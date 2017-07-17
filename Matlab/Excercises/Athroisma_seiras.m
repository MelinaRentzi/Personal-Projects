close all
clear all
clc

% a=1;
% while a<10
%     a=a+1
%     
% end

format long
sum1=0;


for N=1:60
    S=zeros(N,1);
    sum1=0;
for i=1:N
    
      sum1=sum1+ 0.5^i;
      S(i)=0.5^i;
end

total(N,:)= [ N ,sum1 ,sum(S)];
end

% total


sum3=0;
N=0;
while sum3~=1
    sum3=0;
    N=N+1;
    for i=1:N
    
      sum3=sum3+ 0.5^i;
      S(i)=0.5^i;
end
total(N,4)=sum3;
end
total

