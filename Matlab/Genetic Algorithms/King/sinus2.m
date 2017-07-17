clear all
close all
clc
%sto idio sxhma ta prohgoumena
x=linspace(-2*pi,2*pi)
for i=1:8
hold on
y=sin((x/2)*i)

%subplot(4,4,i)
figure(1)
plot(1)
plot(x,y,'r')

% plot(x(y==min(y)),min(y),'o') 
% plot(x(y==max(y)),max(y),'+')
end


w=linspace(-2,2);
z=w.^2-1;
%z=[0 2];
figure(1)
plot(w,z,'b')
