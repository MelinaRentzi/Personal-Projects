clear all
clc


A= randi([0 100] , 20 , 5 )  %pinakas 20x5 me tyxaious akeraious apo to 0 ws to 100

n=length(A);
F=zeros(n,2);

for i=1:n
    F(i,1)=i;
    F(i,2)=sum(A(i,:));    
end

FF=initiate_target(F)