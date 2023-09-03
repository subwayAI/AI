function [bw1,ee]=andy_dege(img)
I1=img(:,:,1);
I1=double(I1);
bw1=edge(I1,'canny');

I1=img(:,:,2);
I1=double(I1);
bw2=edge(I1,'canny');



I1=img(:,:,3);
I1=double(I1);
bw3=edge(I1,'canny');

ee=cat(3,bw1,bw2,bw3);
%figure
%imshow(ee)