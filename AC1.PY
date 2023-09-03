
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

mkpath="E:/fengfa_zengqiang_ac/ban"

# 调用函数
mkdir(mkpath)

mkpath="E:/fengfa_zengqiang_ac/guanbi"

# 调用函数
mkdir(mkpath)


mkpath="E:/fengfa_zengqiang_ac/kai"

# 调用函数
mkdir(mkpath)


mkpath="E:/fengfa_zengqiang_ac1"
mkdir(mkpath)



import cv2
import numpy as np
import matplotlib.pyplot as plt
def cal_dist(hist):
    dist = {}
    for gray in range(256):
        value = 0.0
        for k in range(256):
            value += hist[k][0] * abs(gray - k)
        dist[gray] = value
    return dist

def LC(image_gray):
    image_height = image_gray.shape[0]
    image_width = image_gray.shape[1]
    image_gray_copy = np.zeros((image_height, image_width))
    hist_array = cv2.calcHist([image_gray], [0], None, [256], [0.0, 256.0])  # 直方图，统计图像中每个灰度值的数量
    gray_dist = cal_dist(hist_array)  # 灰度值与其他值的距离
    # print(gray_dist)
    for i in range(image_width):
        for j in range(image_height):
            temp = image_gray[j][i]
            image_gray_copy[j][i] = gray_dist[temp]
    image_gray_copy = (image_gray_copy - np.min(image_gray_copy)) / (np.max(image_gray_copy) - np.min(image_gray_copy))
    return image_gray_copy

def FT(src):
    lab = cv2.cvtColor(src,cv2.COLOR_BGR2LAB)
    gaussian_blur=cv2.GaussianBlur(src,(5,5),0)

    mean_lab = np.mean(lab,axis=(0,1))
    print(mean_lab.shape)

    salient_map = (gaussian_blur - mean_lab)*(gaussian_blur - mean_lab)
    salient_map = (salient_map-np.amin(salient_map))/(np.amax(salient_map)-np.amin(salient_map))
    
    return salient_map




import cv2
import os

def read_path(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(file_pathname+'/'+filename)
        img = cv2.imread(file_pathname+'/'+filename)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        saliency_image = FT(img)
        
        #获取图像原始LBP特征，并显示其统计直方图与特征图像
        #basic_array=lbp.lbp_basic(image_array)
        #lbp.show_basic_hist(basic_array)
        #lbp.show_image(basic_array)
        #cv2.imwrite('Egyptian_cat.jpg', frame_out)

        #plt.figure()
        #plt.imshow(frame_out)


        #Predictions3=Predictions.numpy()
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #plt.show()

        #####save figure
        cv2.imwrite('E:/fengfa_zengqiang_ac/ban'+"/"+filename,saliency_image)       

#注意*处如果包含家目录（home）不能写成~符号代替 
#必须要写成"/home"的格式，否则会报错说找不到对应的目录
#读取的目录
read_path("E:/fengfa_zengqiang/ban")








def read_path1(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(file_pathname+'/'+filename)
        img = cv2.imread(file_pathname+'/'+filename)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        saliency_image = LC(img_gray)
        
        #获取图像原始LBP特征，并显示其统计直方图与特征图像
        #basic_array=lbp.lbp_basic(image_array)
        #lbp.show_basic_hist(basic_array)
        #lbp.show_image(basic_array)
        #cv2.imwrite('Egyptian_cat.jpg', frame_out)

        #plt.figure()
        #plt.imshow(frame_out)


        #Predictions3=Predictions.numpy()
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #plt.show()

        #####save figure
        cv2.imwrite('E:/fengfa_zengqiang_ac/guanbi'+"/"+filename,saliency_image)       

#注意*处如果包含家目录（home）不能写成~符号代替 
#必须要写成"/home"的格式，否则会报错说找不到对应的目录
#读取的目录
read_path1("E:/fengfa_zengqiang/guanbi")





def read_path2(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(file_pathname+'/'+filename)
        img = cv2.imread(file_pathname+'/'+filename)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        saliency_image = LC(img_gray)
        
        #获取图像原始LBP特征，并显示其统计直方图与特征图像
        #basic_array=lbp.lbp_basic(image_array)
        #lbp.show_basic_hist(basic_array)
        #lbp.show_image(basic_array)
        #cv2.imwrite('Egyptian_cat.jpg', frame_out)

        #plt.figure()
        #plt.imshow(frame_out)


        #Predictions3=Predictions.numpy()
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #Predictions3[0][np.argmax(Predictions3[0])]=np.min(Predictions3)
        #plt.show()

        #####save figure
        cv2.imwrite('E:/fengfa_zengqiang_ac/kai'+"/"+filename,saliency_image)       

#注意*处如果包含家目录（home）不能写成~符号代替 
#必须要写成"/home"的格式，否则会报错说找不到对应的目录
#读取的目录
read_path2("E:/fengfa_zengqiang/kai")