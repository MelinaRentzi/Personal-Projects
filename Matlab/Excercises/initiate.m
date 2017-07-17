clear all
clc

A= randi([0 100] , 20 , 5 )  %pinakas 20x5 me tyxaious akeraious apo to 0 ws to 100

F=zeros(length(A),2);
for i=1:length(A)
    F(i,1)=i;
    F(i,2)=sum(A(i,:));
    
end
initialF=F;
F

SortedF=zeros(length(A),2);

    
for i=1:length(A(:,1))
     min=F(1,:)
  
    for j=length(F(:,1)):1
        k=j;
        
        if F(k,2) <= min
            F(k,2)= min
           
        end
       
    end
    SortedF(i,:)= min
    F(SortedF(1,1),:)= []
end

  SortedF

