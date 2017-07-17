close all
clear all
clc

for i=1:10
    i;
    a=randi(19,1,1)+1;
    b(i,:)= [i,a];
    bb=b(i,:);
    y(a)=10;
    
end

b
y


ekf=0;
for i=1:10
    for j=1:10
        if b(i,2)==b(j,2)
             ekf=ekf+1;
             c=[i,j]
        end 
    end
end

ekf=ekf-10;
ekf=ekf/2