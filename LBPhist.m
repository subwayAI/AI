function h=LBPhist(LBP,n)
%获得LBP统计直方图
 
%构造移位前后lbp映射表
map=mapOfP2shiftedP(n);
 
%构造移位后lbp到直方图bin的映射
v=cell2mat(values(map));
v=unique(v);
key=num2cell(v);
value=num2cell(1:length(v));
map2=containers.Map(key,value);
 
h=zeros(length(v),1);
%直方图统计
for i=1:size(LBP,1)
    for j=1:size(LBP,2)
        idx=map2(LBP(i,j));
        h(idx)=h(idx)+1;
    end
end
 