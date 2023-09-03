import torch.nn as nn
import torch
import torch.nn.functional as F

from functools import partial

class ChannelAttention(nn.Module):
    def __init__(self, in_planes, ratio=16):
        super(ChannelAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)

        self.fc1   = nn.Conv2d(in_planes, in_planes // 16, 1, bias=False)
        self.relu1 = nn.ReLU()
        self.fc2   = nn.Conv2d(in_planes // 16, in_planes, 1, bias=False)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = self.fc2(self.relu1(self.fc1(self.avg_pool(x))))
        max_out = self.fc2(self.relu1(self.fc1(self.max_pool(x))))
        out = avg_out + max_out
        return self.sigmoid(out)
#空间注意力机制
class SpatialAttention(nn.Module):
    def __init__(self, kernel_size=7):
        super(SpatialAttention, self).__init__()

        assert kernel_size in (3, 7), 'kernel size must be 3 or 7'
        padding = 3 if kernel_size == 7 else 1

        self.conv1 = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        x = torch.cat([avg_out, max_out], dim=1)
        x = self.conv1(x)
        return self.sigmoid(x)
        
        
class LayerNorm(nn.Module):
    "Construct a layernorm module (See citation for details)."
    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        # mean(-1) 表示 mean(len(x)), 这里的-1就是最后一个维度，也就是hidden_size维
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2
class OctConv(torch.nn.Module):
    """
    This module implements the OctConv paper https://arxiv.org/pdf/1904.05049v1.pdf
    """
    def __init__(self, in_channels=32, out_channels=32, kernel_size=1, stride=1, alpha_in=0.5, alpha_out=0.5):
        super(OctConv, self).__init__()
        self.alpha_in, self.alpha_out, self.kernel_size = alpha_in, alpha_out, kernel_size
        self.H2H, self.L2L, self.H2L, self.L2H = None, None, None, None
        if not (alpha_in == 0.0 and alpha_out == 0.0):
            self.L2L = torch.nn.Conv2d(int(alpha_in * in_channels),
                                       int(alpha_out * out_channels),
                                       kernel_size, stride, kernel_size//2)
        if not (alpha_in == 0.0 and alpha_out == 1.0):
            self.L2H = torch.nn.Conv2d(int(alpha_in * in_channels),
                                       out_channels - int(alpha_out * out_channels),
                                       kernel_size, stride, kernel_size//2)
        if not (alpha_in == 1.0 and alpha_out == 0.0):
            self.H2L = torch.nn.Conv2d(in_channels - int(alpha_in * in_channels),
                                       int(alpha_out * out_channels),
                                       kernel_size, stride, kernel_size//2)
        if not (alpha_in == 1.0 and alpha_out == 1.0):
            self.H2H = torch.nn.Conv2d(in_channels - int(alpha_in * in_channels),
                                       out_channels - int(alpha_out * out_channels),
                                       kernel_size, stride, kernel_size//2)
        self.upsample = torch.nn.Upsample(scale_factor=2, mode='nearest')
        self.avg_pool = partial(torch.nn.functional.avg_pool2d, kernel_size=kernel_size, stride=kernel_size)

    def forward(self, x):
        hf, lf = x,x
        h2h, l2l, h2l, l2h = None, None, None, None
        if self.H2H is not None:
            h2h = self.H2H(hf)
        if self.L2L is not None:
            l2l = self.L2L(lf)
        if self.H2L is not None:
            h2l = self.H2L(self.avg_pool(hf))
        if self.L2H is not None:
            l2h = self.upsample(self.L2H(lf))
        hf_, lf_ = 0, 0
        for i in [h2h, l2h]:
            if i is not None:
                hf_ = hf_ + i
        for i in [l2l, h2l]:
            if i is not None:
                lf_ = lf_ + i
        return hf_, lf_


class GroupBatchnorm2d(nn.Module):
    def __init__(self, c_num:int, 
                 group_num:int = 16, 
                 eps:float = 1e-10
                 ):
        super(GroupBatchnorm2d,self).__init__()
        assert c_num    >= group_num
        self.group_num  = group_num
        self.gamma      = nn.Parameter( torch.randn(c_num, 1, 1)    )
        self.beta       = nn.Parameter( torch.zeros(c_num, 1, 1)    )
        self.eps        = eps

    def forward(self, x):
        N, C, H, W  = x.size()
        x           = x.view(   N, self.group_num, -1   )
        mean        = x.mean(   dim = 2, keepdim = True )
        std         = x.std (   dim = 2, keepdim = True )
        x           = (x - mean) / (std+self.eps)
        x           = x.view(N, C, H, W)
        return x * self.gamma + self.beta


class SRU(nn.Module):
    def __init__(self,
                 oup_channels:int, 
                 group_num:int = 16,
                 gate_treshold:float = 0.5 
                 ):
        super().__init__()
        
        self.gn             = GroupBatchnorm2d( oup_channels, group_num = group_num )
        self.gate_treshold  = gate_treshold
        self.sigomid        = nn.Sigmoid()

    def forward(self,x):
        gn_x        = self.gn(x)
        w_gamma     = F.softmax(self.gn.gamma,dim=0)
        reweigts    = self.sigomid( gn_x * w_gamma )
        # Gate
        info_mask   = w_gamma>self.gate_treshold
        noninfo_mask= w_gamma<=self.gate_treshold
        x_1         = info_mask*reweigts * x
        x_2         = noninfo_mask*reweigts * x
        x           = self.reconstruct(x_1,x_2)
        return x
    
    def reconstruct(self,x_1,x_2):
        x_11,x_12 = torch.split(x_1, x_1.size(1)//2, dim=1)
        x_21,x_22 = torch.split(x_2, x_2.size(1)//2, dim=1)
        return torch.cat([ x_11+x_22, x_12+x_21 ],dim=1)




class CRU(nn.Module):
    '''
    alpha: 0<alpha<1
    '''
    def __init__(self, 
                 op_channel:int,
                 alpha:float = 1/2,
                 squeeze_radio:int = 2 ,
                 group_size:int = 2,
                 group_kernel_size:int = 3,
                 ):
        super().__init__()
        self.up_channel     = up_channel   =   int(alpha*op_channel)
        self.low_channel    = low_channel  =   op_channel-up_channel
        self.squeeze1       = nn.Conv2d(up_channel,up_channel//squeeze_radio,kernel_size=1,bias=False)
        self.squeeze2       = nn.Conv2d(low_channel,low_channel//squeeze_radio,kernel_size=1,bias=False)
        #up
        self.GWC            = nn.Conv2d(up_channel//squeeze_radio, op_channel,kernel_size=group_kernel_size, stride=1,padding=group_kernel_size//2, groups = group_size)
        self.PWC1           = nn.Conv2d(up_channel//squeeze_radio, op_channel,kernel_size=1, bias=False)
        #low
        self.PWC2           = nn.Conv2d(low_channel//squeeze_radio, op_channel-low_channel//squeeze_radio,kernel_size=1, bias=False)
        self.advavg         = nn.AdaptiveAvgPool2d(1)

    def forward(self,x):
        # Split
        up,low  = torch.split(x,[self.up_channel,self.low_channel],dim=1)
        up,low  = self.squeeze1(up),self.squeeze2(low)
        # Transform
        Y1      = self.GWC(up) + self.PWC1(up)
        Y2      = torch.cat( [self.PWC2(low), low], dim= 1 )
        # Fuse
        out     = torch.cat( [Y1,Y2], dim= 1 )
        out     = F.softmax( self.advavg(out), dim=1 ) * out
        out1,out2 = torch.split(out,out.size(1)//2,dim=1)
        return out1+out2

        
        
class AlexNet(nn.Module):
    def __init__(self,norm_layer=LayerNorm, inplanes=32, planes=32, stride=1, padding=1, dilation=1, groups=2, pooling_r=1, num_classes=1000, init_weights=False):
        super(AlexNet, self).__init__()
        
        
        self.k2 = nn.Sequential(  
                    nn.Conv2d(inplanes, planes, kernel_size=1),
                    nn.AvgPool2d(kernel_size=pooling_r, stride=pooling_r),   
                    nn.Conv2d(inplanes, planes, kernel_size=3, stride=1,  
                                padding=padding, dilation=dilation,  
                                groups=groups, bias=False),  
                    #norm_layer(31),  
                    )  
        self.k3 = nn.Sequential(  
                    nn.Conv2d(inplanes, planes, kernel_size=1),
                    nn.Conv2d(inplanes, planes, kernel_size=3, stride=1,  
                                padding=padding, dilation=dilation,  
                                groups=groups, bias=False),  
                    #norm_layer(planes),  
                    )  
        self.k4 = nn.Sequential(  
                    nn.Conv2d(inplanes, planes, kernel_size=1),
                    nn.Conv2d(inplanes, planes, kernel_size=3, stride=stride,  
                                padding=padding, dilation=dilation,  
                                groups=groups, bias=False),  
                    #norm_layer(planes),  
                    )  
  
  
  
        self.features = nn.Sequential(
            nn.Conv2d(3, 12, kernel_size=3, stride=1, padding=2),  # input[3, 224, 224]  output[48, 55, 55]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=1),
            nn.Conv2d(12, 24, kernel_size=3, padding=2),           # output[128, 27, 27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=1),  
            nn.Conv2d(24, 32, kernel_size=5, padding=2),           # output[128, 27, 27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),    
        )
        # output[48, 27, 27]
       
        self.SRU=SRU(oup_channels=32)
        self.CRU=CRU(op_channel=32)
        self.OctConv=OctConv()
        self.classifier = nn.Sequential(
            #nn.Dropout(p=0.5),
            nn.Linear(30752, 32),
            nn.ReLU(inplace=True),
            #nn.Dropout(p=0.5),
            #nn.Linear(2048, 2048),
            #nn.ReLU(inplace=True),
            nn.Linear(32, num_classes),
        )
        if init_weights:
            self._initialize_weights()
            
        # 网络的第一层加入注意力机制
        self.ca = ChannelAttention(32)
        self.sa = SpatialAttention()
        

    def forward(self, x):
        
        x = self.features(x)
        x = self.ca(x) * x
        x = self.sa(x) * x
        #d=self.SRU(x)
        #d1=self.CRU(x)
        #print(d.shape,d1.shape,x.shape)
        #d,d1=self.OctConv(x)
        #print(d.shape,d1.shape,x.shape)
        #x = self.features1(x)
        #x = self.cv(x)
        #identity = x  
  
        #out = torch.sigmoid(torch.add(identity, F.interpolate(self.k2(x), identity.size()[2:]))) # sigmoid(identity + k2)  
        #out = torch.mul(self.k3(x), out) # k3 * sigmoid(identity + k2)  
        #x = self.k4(out) # k4  
        
        x = torch.flatten(x, start_dim=1)
        x = self.classifier(x)
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)
