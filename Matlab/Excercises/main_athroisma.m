clc 
close all 
clear all

x=[rand; rand; rand; rand; rand];
y=[rand; rand; rand; rand; rand];

for i=1:5
  D(i,:)=athrisma(x(i,:),y(i,:));
end
D
