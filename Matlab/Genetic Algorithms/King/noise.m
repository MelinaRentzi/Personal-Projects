close all
clear all
clc


N=101;
x=linspace(-10,10,N);
y1=-x.^2;

% lets make some noise ! 
for i=1:N
    y2(i)=-x(i).^2 + 10*rand(1,1)-5;
end

%lets make ever more noise!!
y3=y2;
r = randi(100,10,1)+1
for i=1:10
    y3(r(i))=y3(r(i))+20;
end


figure(1)
plot(x,y1,'.',x,y2,x,y3)





% 
% % xwris na orisw ta shmeia toy x aksona
% syms xx
% figure(2)
% ezplot(-xx^2 , [-10,10])