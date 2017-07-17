function [D]=distance(A,X,Y)
%oxi kai toso tyxaios pinakas

C=randi(A,X,X);
D=C<Y;
sumCcol=zeros(1,X);
sumCrow=zeros(1,X);
for i=1:X
    sumCcol(i)=sum(D(:,i));
    sumCrow(i)=sum(D(i,:));
    
        if sumCcol(i)==0
        a=randi(X);
        D(a,i)=1;
        C(a,i)=randi(Y);
        sumCcol(i)=1;
        end
        
        if sumCrow(i)==0
        a=randi(X);
        D(i,a)=1;
        C(i,a)=randi(Y);
        sumCrow(i)=1;
        end
    
end    

C;

end
