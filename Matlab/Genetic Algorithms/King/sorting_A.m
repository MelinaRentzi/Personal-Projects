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


for i=10:-1:1
   i-9 
end

t=linspace(0,pi);

for i=1:8
    
    figure(i)
    plot(t,sin(i*t))
%     strcat('y',num2str(i))  %=sin(i*t);
    
    figure(11)
    plot(t,sin(i*t)+2*i)
    hold on
end
    
    