import matplotlib.pyplot as plt
import cv2
 




# 初始化配置
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from skimage import color

from time import time
from IPython.display import HTML
#from seam_carving import energy_function
#%matplotlib inline
plt.rcParams['figure.figsize'] = (30.0, 24.0) # 设置默认尺寸
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


from skimage import io, util
import cv2
# 载入图片
def nengliang(img):
    #img = io.imread('yolo.jpg')
    #img = util.img_as_float(img)
    x=img[:,:,0]



    # 计算图像能量
    #start = time()
    energy1 = energy_function(x)
    
    x=img[:,:,1]



    # 计算图像能量
    #start = time()
    energy2 = energy_function(x)
    
    
    x=img[:,:,2]



    # 计算图像能量
    #start = time()
    energy3 = energy_function(x)
    
    energy = cv2.merge([energy1 ,energy2,energy3 ]) #前面分离出来的三个通道 
    
    return energy 
#end = time()

#print("能量函数耗时: %f 秒." % (end - start))

#plt.title('Energy')
#plt.axis('off')
#plt.imshow(energy)
#plt.show()






def mkdir(path):

    # 引入模块

    import os

  

    # 去除首位空格

    path=path.strip()

    # 去除尾部 \ 符号

    path=path.rstrip("\\")

  

    # 判断路径是否存在

    # 存在     True

    # 不存在   False

    isExists=os.path.exists(path)

  

    # 判断结果

    if not isExists:

        # 如果不存在则创建目录

        # 创建目录操作函数

        os.makedirs(path)

  

        print (path+' 创建成功')

        return True

    else:

        # 如果目录存在则不创建，并提示目录已存在

        print (path+' 目录已存在')

        return False

  

# 定义要创建的目录

mkpath="E:/fengfa_zengqiang_hsv/ban"

# 调用函数
mkdir(mkpath)

mkpath="E:/fengfa_zengqiang_hsv/guanbi"

# 调用函数
mkdir(mkpath)


mkpath="E:/fengfa_zengqiang_hsv/kai"

# 调用函数
mkdir(mkpath)



mkpath="E:/fengfa_zengqiang_hsv1"

# 调用函数
mkdir(mkpath)


import cv2
import os

def read_path(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(filename)
        original_img = cv2.imread(file_pathname+'/'+filename)
        print(original_img.shape)
        ####change to gray
      #（下面第一行是将RGB转成单通道灰度图，第二步是将单通道灰度图转成3通道灰度图）
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #image_np=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        frame_out= cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
        #frame_out=nengliang(original_img )
        #original_img=cv2.imread('1.png')
        #heatmap1 = cv2.resize(heatmap[0], (original_img.shape[1], original_img.shape[0]), interpolation=cv2.INTER_CUBIC)
        #heatmap1 = np.uint8(255*heatmap1)
        #heatmap1 = cv2.applyColorMap(heatmap1, cv2.COLORMAP_JET)
        #frame_out=cv2.addWeighted(original_img,0.5,heatmap1,0.5,0)
        #cv2.imwrite('Egyptian_cat.jpg', frame_out)

        #plt.figure()
        #plt.imshow(frame_out)


        #Predictions3=Predictions.numpy()
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #plt.show()

        #####save figure
        cv2.imwrite('E:/fengfa_zengqiang_hsv/ban'+"/"+filename,frame_out)       

#注意*处如果包含家目录（home）不能写成~符号代替 
#必须要写成"/home"的格式，否则会报错说找不到对应的目录
#读取的目录
read_path("E:/fengfa_zengqiang/ban")



def read_path1(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(filename)
        original_img = cv2.imread(file_pathname+'/'+filename)
        print(original_img.shape)
        ####change to gray
      #（下面第一行是将RGB转成单通道灰度图，第二步是将单通道灰度图转成3通道灰度图）
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #image_np=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        frame_out= cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
        #frame_out=nengliang(original_img )
        #original_img=cv2.imread('1.png')
        #heatmap1 = cv2.resize(heatmap[0], (original_img.shape[1], original_img.shape[0]), interpolation=cv2.INTER_CUBIC)
        #heatmap1 = np.uint8(255*heatmap1)
        #heatmap1 = cv2.applyColorMap(heatmap1, cv2.COLORMAP_JET)
        #frame_out=cv2.addWeighted(original_img,0.5,heatmap1,0.5,0)
        #cv2.imwrite('Egyptian_cat.jpg', frame_out)

        #plt.figure()
        #plt.imshow(frame_out)


        #Predictions3=Predictions.numpy()
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #plt.show()

        #####save figure
        cv2.imwrite('E:/fengfa_zengqiang_hsv/kai'+"/"+filename,frame_out)       

#注意*处如果包含家目录（home）不能写成~符号代替 
#必须要写成"/home"的格式，否则会报错说找不到对应的目录
#读取的目录
read_path1("E:/fengfa_zengqiang/kai")



def read_path2(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(filename)
        original_img = cv2.imread(file_pathname+'/'+filename)
        print(original_img.shape)
        ####change to gray
      #（下面第一行是将RGB转成单通道灰度图，第二步是将单通道灰度图转成3通道灰度图）
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #image_np=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        frame_out= cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
        #frame_out=nengliang(original_img )
        #original_img=cv2.imread('1.png')
        #heatmap1 = cv2.resize(heatmap[0], (original_img.shape[1], original_img.shape[0]), interpolation=cv2.INTER_CUBIC)
        #heatmap1 = np.uint8(255*heatmap1)
        #heatmap1 = cv2.applyColorMap(heatmap1, cv2.COLORMAP_JET)
        #frame_out=cv2.addWeighted(original_img,0.5,heatmap1,0.5,0)
        #cv2.imwrite('Egyptian_cat.jpg', frame_out)

        #plt.figure()
        #plt.imshow(frame_out)


        #Predictions3=Predictions.numpy()
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #plt.show()

        #####save figure
        cv2.imwrite('E:/fengfa_zengqiang_hsv/guanbi'+"/"+filename,frame_out)       

#注意*处如果包含家目录（home）不能写成~符号代替 
#必须要写成"/home"的格式，否则会报错说找不到对应的目录
#读取的目录
read_path2("E:/fengfa_zengqiang/guanbi")
