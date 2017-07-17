clear all
close all
clc

A=randi(100,1,18)


megisto=zeros(1,2);
megisto(1,1)=1;
megisto(1,2)=A(1);
for i=1:length(A)
    if A(i)>=megisto;
      megisto= [ i , A(i) ]
           end
    
end



    