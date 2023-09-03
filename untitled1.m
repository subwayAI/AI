function varargout = untitled1(varargin)
% UNTITLED1 MATLAB code for untitled1.fig
%      UNTITLED1, by itself, creates a new UNTITLED1 or raises the existing
%      singleton*.
%
%      H = UNTITLED1 returns the handle to a new UNTITLED1 or the handle to
%      the existing singleton*.
%
%      UNTITLED1('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in UNTITLED1.M with the given input arguments.
%
%      UNTITLED1('Property','Value',...) creates a new UNTITLED1 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before untitled1_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to untitled1_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help untitled1

% Last Modified by GUIDE v2.5 02-Sep-2023 18:25:54

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @untitled1_OpeningFcn, ...
                   'gui_OutputFcn',  @untitled1_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before untitled1 is made visible.
function untitled1_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to untitled1 (see VARARGIN)

% Choose default command line output for untitled1
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes untitled1 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = untitled1_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python ac1.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


if ~exist('D:\zengqianghog3','dir')
    mkdir('D:\zengqianghog3');
    disp('successfully create directory image!');
end


if ~exist('D:\zengqianghog2\ban','dir')
    mkdir('D:\zengqianghog2\ban');
    disp('successfully create directory image!');
end

if ~exist('D:\zengqianghog2\guanbi','dir')
    mkdir('D:\zengqianghog2\guanbi');
    disp('successfully create directory image!');
end



if ~exist('D:\zengqianghog2\kai','dir')
    mkdir('D:\zengqianghog2\kai');
    disp('successfully create directory image!');
end


impath_to ='zengqianghog/';

A='D:\fengfa_zengqiang\ban\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    strcat(i,A)
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   img = image;%read('239_1.0.jpg');
 ax=hog1(img);
 %imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqianghog2\ban\',files(i).name)
  imwrite(ax,ee)
end





A='D:\fengfa_zengqiang\guanbi\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
      strcat(i,A)
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   img = image;%read('239_1.0.jpg');
 ax=hog1(img);
 %imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqianghog2\guanbi\',files(i).name)
  imwrite(ax,ee)
end




A='D:\fengfa_zengqiang\kai\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
   strcat(i,A)
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   img = image;%read('239_1.0.jpg');
 ax=hog1(img);
 %imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqianghog2\kai\',files(i).name)
  imwrite(ax,ee)
end


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

ksize = 50;     % kernel size
d = ksize/2;
lambda = 6;     % wavelength
theta = [pi/2];      % orientation
phase = 0;
sigma = 4;      % variation
ratio = 0.5;    % spatial aspect ratio
 




if ~exist('D:\zengqianggabor\ban','dir')
    mkdir('D:\zengqianggabor\ban');
    disp('successfully create directory image!');
end

if ~exist('D:\zengqianggabor\guanbi','dir')
    mkdir('D:\zengqianggabor\guanbi');
    disp('successfully create directory image!');
end



if ~exist('D:\zengqianggabor\kai','dir')
    mkdir('D:\zengqianggabor\kai');
    disp('successfully create directory image!');
end


impath_to ='zengqianggabor/';

A='D:\fengfa_zengqiang\ban\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1
    tt=[]
    %for 
    i
  
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
 %ax=zengqianggabor(img);
 
 I =  image;%read('239_1.0.jpg'
I = rgb2gray(I);
 
Ig_cell = cell(1,length(theta));
for k = 1:length(theta)
    Ig_cell{1,k} = gabor_imgProcess_peng(I,ksize,lambda,theta(k),phase,sigma,ratio);
end
 

 figure
 imshow(Ig_cell{1,1})
 
 
 saveas(gcf, 'save.jpg'); %保存当前窗口的图像
  a=imread('save.jpg');
  a=a(40:138,117:220.0,:);
  figure
 imshow(a)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqianggabor\ban\',files(i).name)
  imwrite(a,ee)
end
 close all
 
 
 
 
 
 
 
 A='D:\fengfa_zengqiang\guanbi\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1
    tt=[]
    %for 
    i
  
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
 %ax=zengqianggabor(img);
 
 I =  image;%read('239_1.0.jpg'
I = rgb2gray(I);
 
Ig_cell = cell(1,length(theta));
for k = 1:length(theta)
    Ig_cell{1,k} = gabor_imgProcess_peng(I,ksize,lambda,theta(k),phase,sigma,ratio);
end
 

 figure
 imshow(Ig_cell{1,1})
 
 
 saveas(gcf, 'save.jpg'); %保存当前窗口的图像
  a=imread('save.jpg');
  a=a(40:138,117:220.0,:);
  figure
 imshow(a)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqianggabor\guanbi\',files(i).name)
  imwrite(a,ee)
end
 close all
 
 
 
 
 A='D:\fengfa_zengqiang\kai\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1
    tt=[]
    %for 
    i
  
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
 %ax=zengqianggabor(img);
 
 I =  image;%read('239_1.0.jpg'
I = rgb2gray(I);
 
Ig_cell = cell(1,length(theta));
for k = 1:length(theta)
    Ig_cell{1,k} = gabor_imgProcess_peng(I,ksize,lambda,theta(k),phase,sigma,ratio);
end
 

 figure
 imshow(Ig_cell{1,1})
 
 
 saveas(gcf, 'save.jpg'); %保存当前窗口的图像
  a=imread('save.jpg');
  a=a(40:138,117:220.0,:);
  figure
 imshow(a)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqianggabor\kai\',files(i).name)
  imwrite(a,ee)
end
 close all
 
 


% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

if ~exist('D:\zengqiang3weikpca\ban','dir')
    mkdir('D:\zengqiang3weikpca\ban');
    disp('successfully create directory image!');
end

if ~exist('D:\zengqiang3weikpca\guanbi','dir')
    mkdir('D:\zengqiang3weikpca\guanbi');
    disp('successfully create directory image!');
end



if ~exist('D:\zengqiang3weikpca\kai','dir')
    mkdir('D:\zengqiang3weikpca\kai');
    disp('successfully create directory image!');
end


if ~exist('D:\zengqiang3weikpca1','dir')
    mkdir('D:\zengqiang3weikpca1');
    disp('successfully create directory image!');
end



impath_to ='zengqiang3weikpca/';

A='D:\fengfa_zengqiang\ban\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
   %outPic=pca_comp_show(mul)
 ax=pca_comp_show(image);
 imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqiang3weikpca\ban\',files(i).name)
  imwrite(ax,ee)
end





A='D:\fengfa_zengqiang\guanbi\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
   %outPic=pca_comp_show(mul)
 ax=pca_comp_show(image);
 imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqiang3weikpca\guanbi\',files(i).name)
  imwrite(ax,ee)
end







A='D:\fengfa_zengqiang\kai\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
   %outPic=pca_comp_show(mul)
 ax=pca_comp_show(image);
 imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqiang3weikpca\kai\',files(i).name)
  imwrite(ax,ee)
end


% --- Executes on button press in pushbutton6.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

if ~exist('D:\zengqianglbp\ban','dir')
    mkdir('D:\zengqianglbp\ban');
    disp('successfully create directory image!');
end

if ~exist('D:\zengqianglbp\guanbi','dir')
    mkdir('D:\zengqianglbp\guanbi');
    disp('successfully create directory image!');
end



if ~exist('D:\zengqianglbp\kai','dir')
    mkdir('D:\zengqianglbp\kai');
    disp('successfully create directory image!');
end


impath_to ='zengqianglbp/';

A='D:\fengfa_zengqiang\ban\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
  
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   img = image;%read('239_1.0.jpg');
 %ax=zengqianglbp(img);
 
 img=image(:,:,1);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x1=lbp/(2^n-1);

 img=image(:,:,1);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x2=lbp/(2^n-1);


 img=image(:,:,3);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x3=lbp/(2^n-1);

ss=cat(3,x1,x2,x3);

 %imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqianglbp\ban\',files(i).name)
  imwrite(ss,ee)
end
%——————






A='D:\fengfa_zengqiang\guanbi\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   img = image;%read('239_1.0.jpg');
 %ax=zengqianglbp(img);
 
img=image(:,:,1);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x1=lbp/(2^n-1);

 img=image(:,:,1);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x2=lbp/(2^n-1);


 img=image(:,:,3);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x3=lbp/(2^n-1);

ss=cat(3,x1,x2,x3);
   ee=strcat('D:\zengqianglbp\guanbi\',files(i).name)
  imwrite(ss,ee)
end
%——————




A='D:\fengfa_zengqiang\kai\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
   
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   img = image;%read('239_1.0.jpg');
 %ax=zengqianglbp(img);
 
 img=image(:,:,1);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x1=lbp/(2^n-1);

 img=image(:,:,1);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x2=lbp/(2^n-1);


 img=image(:,:,3);
radius=2;
n=16;
lbp=LBP(img,radius,n);
%figure,imshow(lbp/(2^n-1));
%imwrite(lbp/(2^n-1),'res.bmp');
x3=lbp/(2^n-1);

ss=cat(3,x1,x2,x3);
   ee=strcat('D:\zengqianglbp\kai\',files(i).name)
  imwrite(ss,ee)
end
%——————


% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

if ~exist('D:\zengqiangcandy\ban','dir')
    mkdir('D:\zengqiangcandy\ban');
    disp('successfully create directory image!');
end

if ~exist('D:\zengqiangcandy\guanbi','dir')
    mkdir('D:\zengqiangcandy\guanbi');
    disp('successfully create directory image!');
end



if ~exist('D:\zengqiangcandy\kai','dir')
    mkdir('D:\zengqiangcandy\kai');
    disp('successfully create directory image!');
end


if ~exist('D:\zengqiangcandy1','dir')
    mkdir('D:\zengqiangcandy1');
    disp('successfully create directory image!');
end



impath_to ='zengqiangcandy/';

A='D:\fengfa_zengqiang\ban\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
   %outPic=my_pca(mul)
[bw,ax]=andy_dege(image);

 %imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqiangcandy\ban\',files(i).name)
  imwrite(ax,ee)
end




A='D:\fengfa_zengqiang\guanbi\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
   %outPic=my_pca(mul)
[bw,ax]=andy_dege(image);
%figure(1)
 %imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqiangcandy\guanbi\',files(i).name)
  imwrite(ax,ee)
end





A='D:\fengfa_zengqiang\kai\'
SamplePath1 = A% 'data\';  %存储图像的路径
fileExt = '*.jpg';  %待读取图像的后缀名
%获取所有路径
files = dir(fullfile(SamplePath1,fileExt)); 
len1 = size(files,1);
%遍历路径下每一幅图像

for i=1:len1;
    tt=[]
    %for 
    i
    
    
   fileName = strcat(SamplePath1,files(i).name); 
   image = imread(fileName);
  % image = imresize(image,[61 61]);
   %img = image;%read('239_1.0.jpg');
   %outPic=my_pca(mul)
[bw,ax]=andy_dege(image);

 %imshow(ax)
   %norubbish_data(:,:,:,i) = image;
   ee=strcat('D:\zengqiangcandy\kai\',files(i).name)
  imwrite(ax,ee)
end


% --- Executes on button press in pushbutton8.
function pushbutton8_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python 2.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python YANSE.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton13.
function pushbutton13_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python train3.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化

% --- Executes on button press in pushbutton10.
function pushbutton10_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
all=[]
lei=[]

s='../trainkaihedu/train/1/'
file_path = s;% 图像文件夹路径
img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
lei=[lei;img_num];
if img_num > 0 %有满足条件的图像
        for j = 1:img_num %逐一读取图像
            image_name = img_path_list(j).name;% 图像名
            image =  imread(strcat(file_path,image_name));
            fprintf('%d %d %s\n',i,j,strcat(file_path,image_name));% 显示正在处理的图像名
            %图像处理过程 省略
            s1=(image);
            s1=rgb2gray(s1);
            s1=imresize(s1,[12 12]);
            s1=imresize(s1,[1 144]);
            all=[all;s1];
        end
end


s='../trainkaihedu/train/2-1/'
file_path = s;% 图像文件夹路径
img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
lei=[lei;img_num];
if img_num > 0 %有满足条件的图像
        for j = 1:img_num %逐一读取图像
            image_name = img_path_list(j).name;% 图像名
            image =  imread(strcat(file_path,image_name));
            fprintf('%d %d %s\n',i,j,strcat(file_path,image_name));% 显示正在处理的图像名
            %图像处理过程 省略
            s1=(image);
            s1=rgb2gray(s1);
            s1=imresize(s1,[12 12]);
            s1=imresize(s1,[1 144]);
            all=[all;s1];
        end
end




s='../trainkaihedu/train/3/'
file_path = s;% 图像文件夹路径
img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
lei=[lei;img_num];
if img_num > 0 %有满足条件的图像
        for j = 1:img_num %逐一读取图像
            image_name = img_path_list(j).name;% 图像名
            image =  imread(strcat(file_path,image_name));
            fprintf('%d %d %s\n',i,j,strcat(file_path,image_name));% 显示正在处理的图像名
            %图像处理过程 省略
            s1=(image);
            s1=rgb2gray(s1);
            s1=imresize(s1,[12 12]);
            s1=imresize(s1,[1 144]);
            all=[all;s1];
        end
end

save all.mat all lei



all=[]
lei=[]

s='../trainkaihedu/san/1/'
file_path = s;% 图像文件夹路径
img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
lei=[lei;img_num];
if img_num > 0 %有满足条件的图像
        for j = 1:img_num %逐一读取图像
            image_name = img_path_list(j).name;% 图像名
            image =  imread(strcat(file_path,image_name));
            fprintf('%d %d %s\n',i,j,strcat(file_path,image_name));% 显示正在处理的图像名
            %图像处理过程 省略
            s1=(image);
            s1=rgb2gray(s1);
            s1=imresize(s1,[12 12]);
            s1=imresize(s1,[1 144]);
            all=[all;s1];
        end
end


s='../trainkaihedu/san/2-1/'
file_path = s;% 图像文件夹路径
img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
lei=[lei;img_num];
if img_num > 0 %有满足条件的图像
        for j = 1:img_num %逐一读取图像
            image_name = img_path_list(j).name;% 图像名
            image =  imread(strcat(file_path,image_name));
            fprintf('%d %d %s\n',i,j,strcat(file_path,image_name));% 显示正在处理的图像名
            %图像处理过程 省略
            s1=(image);
            s1=rgb2gray(s1);
            s1=imresize(s1,[12 12]);
            s1=imresize(s1,[1 144]);
            all=[all;s1];
        end
end




s='../trainkaihedu/san/3/'
file_path = s;% 图像文件夹路径
img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
lei=[lei;img_num];
if img_num > 0 %有满足条件的图像
        for j = 1:img_num %逐一读取图像
            image_name = img_path_list(j).name;% 图像名
            image =  imread(strcat(file_path,image_name));
            fprintf('%d %d %s\n',i,j,strcat(file_path,image_name));% 显示正在处理的图像名
            %图像处理过程 省略
            s1=(image);
            s1=rgb2gray(s1);
            s1=imresize(s1,[12 12]);
            s1=imresize(s1,[1 144]);
            all=[all;s1];
        end
end

save as.mat all lei


% 载入测试数据wine,其中包含的数据为classnumber = 3,winD:178*13的矩阵,wine_labes:178*1的列向量
load all.mat;
c=double(all);
tlei=[ones(lei(1),1);2*ones(lei(2),1);3*ones(lei(3),1)]
load as.mat 
c1=double(all);
tlei1=[ones(lei(1),1);2*ones(lei(2),1);3*ones(lei(3),1)]

save mat.mat c c1 tlei tlei1
% 将第一类的1-30,第二类的60-95,第三类的131-153做为训练集
train_wine = c%出来
train_wine_labels =tlei;%;wine_labels(60:95);wine_labels(131:153)];
% 将第一类的31-59,第二类的96-130,第三类的154-178做为测试集
test_wine = c1%;wine(96:130,:);wine(154:178,:)];
% 相应的测试集的标签也要分离出来
test_wine_labels =tlei1
%;wine_labels(96:130);wine_labels(154:178)];
figure
plot(c)
figure
plot(tlei)
%% 数据预处理
% 数据预处理,将训练集和测试集归一化到[0,1]区间

[mtrain,ntrain] = size(train_wine);
[mtest,ntest] = size(test_wine);

dataset = [train_wine;test_wine];
% mapminmax为MATLAB自带的归一化函数
[dataset_scale,ps] = mapminmax(dataset',0,1);
dataset_scale = dataset_scale';

train_wine = dataset_scale(1:mtrain,:);
test_wine = dataset_scale( (mtrain+1):(mtrain+mtest),: );
%% SVM网络训练
model = svmtrain(train_wine_labels, train_wine, '-c 0.11202 -g 20.1');

%% SVM网络预测
[predict_label, accuracy] = svmpredict(test_wine_labels, test_wine, model);

%% 结果分析

% 测试集的实际分类和预测分类图
% 通过图可以看出只有一个测试样本是被错分的
figure;
hold on;
plot(test_wine_labels,'o');
plot(predict_label,'r*');
xlabel('SAMPLE','FontSize',12);
ylabel('label','FontSize',12);
legend('real','predict');
title('classify','FontSize',12);
grid on;
cc=sum(test_wine_labels-predict_label==0)/length(test_wine_labels)
title(['train data svm ,acc:',num2str(cc)])

figure %创建混淆矩阵图
cm = confusionchart(test_wine_labels,predict_label)

cm.Title = 'svm Confusion Matrix';


% --- Executes on button press in pushbutton11.
function pushbutton11_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
load mat.mat 
p_train=c'
p_test=c1'
%% 将期望类别转换为向量
t_train=tlei
t_test=tlei1
t_train=ind2vec(t_train');
t_train_temp=tlei %Train(:,4)';
%% 使用newpnn函数建立PNN SPREAD选取为1.5
Spread=10.005;
net=newpnn(p_train,t_train,Spread)

%% 训练数据回代 查看网络的分类效果

% Sim函数进行网络预测
Y=sim(net,p_train);
% 将网络输出向量转换为指针
Yc=vec2ind(Y);

%% 通过作图 观察网络对训练数据分类效果
figure

stem(1:length(Yc),Yc,'bo')
hold on
stem(1:length(Yc),t_train_temp,'r*')
xlabel('sample')
ylabel('result')

H=Yc-t_train_temp';

s=sum(H==0)
s1s=s/length(Yc)

title(['train data PNN ,acc:',num2str(s1s)])



%% 网络预测未知数据效果
Y2=sim(net,p_test);
Y2c=vec2ind(Y2);
figure(12)
stem(1:length(Y2c),Y2c,'b^')
hold on
stem(1:length(Y2c),t_test,'r*')
stem(1:length(Y2c),t_test,'r*')
title('test data PNN result ')
xlabel('sample number')
ylabel('result')
set(gca,'Ytick',[1:5])
s=sum(Y2c==t_test')
ss=s/length(Y2c)
title(['test data PNN ,acc:',num2str(ss)])

figure %创建混淆矩阵图
cm = confusionchart(t_test',Y2c)

cm.Title = 'pnn test data test data Confusion Matrix';

% --- Executes on button press in pushbutton12.
function pushbutton12_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python train1.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton14.
function pushbutton14_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python train2.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton15.
function pushbutton15_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton15 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python traincbam.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton16.
function pushbutton16_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton16 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python trainbam.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton17.
function pushbutton17_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton17 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python trainbam1.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton18.
function pushbutton18_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton18 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python trainECA.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton19.
function pushbutton19_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton19 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
c= system('python trainsk.py ')%%%表示运行ac程序 使得数据可以
%%数据可以批量进行ac处理变化


% --- Executes on button press in pushbutton20.
function pushbutton20_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton20 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


load mat.mat c c1 tlei tlei1
% 将第一类的1-30,第二类的60-95,第三类的131-153做为训练集
train_wine = c%出来
train_wine_labels =tlei;%;wine_labels(60:95);wine_labels(131:153)];
% 将第一类的31-59,第二类的96-130,第三类的154-178做为测试集
test_wine = c1%;wine(96:130,:);wine(154:178,:)];
% 相应的测试集的标签也要分离出来
test_wine_labels =tlei1
%;wine_labels(96:130);wine_labels(154:178)];
figure
plot(c)
figure
plot(tlei)
%% 数据预处理
% 数据预处理,将训练集和测试集归一化到[0,1]区间

[mtrain,ntrain] = size(train_wine);
[mtest,ntest] = size(test_wine);

dataset = [train_wine;test_wine];
% mapminmax为MATLAB自带的归一化函数
[dataset_scale,ps] = mapminmax(dataset',0,1);
dataset_scale = dataset_scale';

train_wine = dataset_scale(1:mtrain,:);
test_wine = dataset_scale( (mtrain+1):(mtrain+mtest),: );


net = feedforwardnet(5, 'traingd'); 
%是'5'是指隐含层有5个神经元，这里只有一个隐含层，多个隐含层神经元的个数设置为[5,3,...]
P=train_wine',
T=test_wine'
Y1=train_wine_labels'% =tlei1
Y2=test_wine_labels' %=tlei1
net.trainParam.lr = 0.01; %学习速率
net.trainParam.epochs = 50; %最大训练次数
net.trainParam.goal = 1e-6; %最小误差，达到该精度，停止训练
net.trainParam.show = 50; %每50次展示训练结果
net = train(net, P, Y1); %训练
Y = net(P); %输出
%perf = perform(net, Y, Y1);%误差
subplot(121)
plot(round(Y))
hold on
plot(Y1, 'r-')


subplot(122)
Y = net(T); %输出
%perf = perform(net, Y, Y2);%误差
plot(Y2)
hold on
plot(round(Y))

pause(1)
close all

