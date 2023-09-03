import torch.nn as nn
import torch

import numpy as np
import torch
from torch import nn
from torch.nn import init

import numpy as np
import torch
from torch import nn
from torch.nn import init



import numpy as np
import torch
from torch import nn
from torch.nn import init

class Flatten(nn.Module):
    def forward(self,x):
        return x.view(x.shape[0],-1)

import torch.nn as nn
import torch

class SKConv(nn.Module):
    def __init__(self, in_ch, M=3, G=1, r=4, stride=1, L=32) -> None:
        super().__init__()
        """ Constructor
        Args:
        in_ch: input channel dimensionality.
        M: the number of branchs.
        G: num of convolution groups.
        r: the radio for compute d, the length of z.
        stride: stride, default 1.
        L: the minimum dim of the vector z in paper, default 32.
        """
        d = max(int(in_ch/r), L)  # 用来进行线性层的输出通道，当输入数据In_ch很大时，用L就有点丢失数据了。
        self.M = M
        self.in_ch = in_ch
        self.convs = nn.ModuleList([])
        for i in range(M):
            self.convs.append(
                nn.Sequential(
                nn.Conv2d(in_ch, in_ch, kernel_size=3+i*2, stride=stride, padding = 1+i, groups=G),
                nn.BatchNorm2d(in_ch),
                nn.ReLU(inplace=True)
                )
            )
        # print("D:", d)
        self.fc = nn.Linear(in_ch, d)
        self.fcs = nn.ModuleList([])
        for i in range(M):
            self.fcs.append(nn.Linear(d, in_ch))
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        for i, conv in enumerate(self.convs):  # 第一部分，每个分支的数据进行相加,虽然这里使用的是torch.cat，但是后面又用了unsqueeze和sum进行升维和降维
            fea = conv(x).clone().unsqueeze_(dim=1).clone()   # 这里在1这个地方新增了一个维度  16*1*64*256*256
            if i == 0:
                feas = fea
            else:
                feas = torch.cat([feas.clone(), fea], dim=1)  # feas.shape  batch*M*in_ch*W*H
        fea_U = torch.sum(feas.clone(), dim=1)  # batch*in_ch*H*W
        fea_s = fea_U.clone().mean(-1).mean(-1)  # Batch*in_ch
        fea_z = self.fc(fea_s)  # batch*in_ch-> batch*d
        for i, fc in enumerate(self.fcs):
            # print(i, fea_z.shape)
            vector = fc(fea_z).clone().unsqueeze_(dim=1)  # batch*d->batch*in_ch->batch*1*in_ch
            # print(i, vector.shape)
            if i == 0:
                attention_vectors = vector
            else:
                attention_vectors = torch.cat([attention_vectors.clone(), vector], dim=1)  # 同样的相加操作 # batch*M*in_ch
        attention_vectors = self.softmax(attention_vectors.clone()) # 对每个分支的数据进行softmax操作
        attention_vectors = attention_vectors.clone().unsqueeze(-1).unsqueeze(-1) # ->batch*M*in_ch*1*1
        fea_v = (feas * attention_vectors).clone().sum(dim=1) # ->batch*in_ch*W*H
        return fea_v


        
        
        
class AlexNet(nn.Module):
    def __init__(self, num_classes=1000, init_weights=False):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 48, kernel_size=11, stride=4, padding=2),  # input[3, 224, 224]  output[48, 55, 55]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2)
        )
        # output[48, 27, 27]
        self.features1 = nn.Sequential(
            nn.Conv2d(48, 128, kernel_size=5, padding=2),           # output[128, 27, 27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 13, 13]
            nn.Conv2d(128, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True)
        )
        self.cv=nn.Sequential(
            nn.Conv2d(192, 128, kernel_size=3, padding=1),          # output[128, 13, 13]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 6, 6]
        )
        
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(128 * 1 * 1, 2048),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, num_classes),
        )
        if init_weights:
            self._initialize_weights()
        #self.SpatialGroupEnhance= BAMBlock(channel=48,reduction=16,dia_val=2)
        #(groups=8)x = self.features(x)
        self.sk = SKConv(in_ch=48,  M=3, G=1, r=2)
    def forward(self, x):
        x = self.features(x)
        #print(x.shape)
        x=self.sk(x)
        #print(x.shape)
        x = self.features1(x)
        x = self.cv(x)
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
