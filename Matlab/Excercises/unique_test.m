clear all
clc


% n=100
% for i=1:N
% 
% A(i,:)=diplwm(a)
% end





A= [      1     0     1
     1     1     0
     0     1     1
     1     0     1
     1     1     1
     0     0     1
     0     0     1
     1     1     0
     1     1     1
     1     1     0 ]
 
 
 [sort , ia , ic ]=unique(A,'rows')
 [a , b ]=size(ia)
 count_A=zeros(a,1);
 for i=1:a
     for j=1:length(A)
         if ic(j)==i
             count_A(i)=count_A(i)+1;
         end        
     end
 end
 
 
B= horzcat(sort,count_A)