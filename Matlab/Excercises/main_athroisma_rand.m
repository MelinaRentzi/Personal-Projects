clc 
close all 
clear all

x=[1 2; 4 5; 6 7; 9 8 ; 2 10];
y=[3 4; 0 1; 5 2; 9 2; 7 5];

for i=1:5
  D(i,:)=athrisma(x(i,:),y(i,:));
end
D
