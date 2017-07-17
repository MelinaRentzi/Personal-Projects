function F=initiate5(F)


A= randi([0 100] , 20 , 5 )  %pinakas 20x5 me tyxaious akeraious apo to 0 ws to 100
n=length(A);
F=zeros(n,2);

for i=1:n
    F(i,1)=i;
    F(i,2)=sum(A(i,:));    
end

initialF=F;
F

    for j=1:(n-1)
        
        imin=score_min(F,j)
        F=swap_line(F,imin,j)
        
    end

end