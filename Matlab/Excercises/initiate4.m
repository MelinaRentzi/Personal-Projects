function F=initiate4(F)


A= randi([0 100] , 20 , 5 )  %pinakas 20x5 me tyxaious akeraious apo to 0 ws to 100
n=length(A);
F=zeros(n,2);

for i=1:n
    F(i,1)=i;
    F(i,2)=sum(A(i,:));    
end
initialF=F
F

for j=1:(n-1)
    imin=j;
    for i=(j+1):n
        if F(i,2)<=F(imin,2)
            imin=i;
        end
    end
    if (imin~=j)
       
        F=swap_line(F,imin,j);
    end
end

end