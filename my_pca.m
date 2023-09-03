
function [vector ,value,tempMul] = my_pca(mul)
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
% % % 该函数用来实现多光谱图像的PCA算法
% % %    param：
% % %          mul--输入的多光谱图像也可以是多通道的
% % %          value--特征值从大到小排列
% % %          vector--特征向量对应特征值排列，一列是一个特征向量
% % %          tempMul--mul的reshape成pixels*bands形式的2维矩阵
% % % 
% % %  @author：chaolei
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
mul=double(mul)/255;
[r ,c ,bands]=size(mul);
pixels = r*c;
% reshape成pixels*channel
mul = reshape(mul, [pixels,bands]);
tempMul = mul;
% 求各通道的均值
meanValue =  mean(mul,1);

% 数据去中心化
mul = mul - repmat(meanValue,[r*c,1]);
% 求协方差矩阵
correlation = (mul'*mul)/pixels;
%求特征向量与特征值
[vector ,value] = eig(correlation);
% 特征值和特征向量从大到小排序
vector = fliplr(vector);
value = fliplr(value);
value = flipud(value);

end

