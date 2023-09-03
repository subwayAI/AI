function  comp=pca_comp_show(mul)
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
% % % 该函数用来显示经过PCA压缩后的图像
% % %  param：
% % %     mul--输入的多光谱或者高光谱图像  
% % %     n--指定用多少个主成分
% % % @author：chaolei
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
n=1
[vector ,value,tempMul] = my_pca(mul);
% 使用其中最重要的n个主成分,并还原到原图像大小
% PCA逆变换
% 原始数据reshape*特征向量矩阵*特征向量矩阵'
re = tempMul*vector(:,1:n)*vector(:,1:n)';
[r,c,bands] =size(mul);
comp = reshape(re,[r,c,bands]);

str =sprintf('%d%s',n,'个主成分');
figure(1);imshow(comp);title(str);
end
