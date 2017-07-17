%Care and Share Algorithm
function Acare=caretaker(A,C)

 
 regionsum=0;
 n=length(C);       

           while regionsum ~=1
           i=1;
           CC=C; 
           
           
          if sum(A)==0
              A(randi([1,10],1,1))=1;
          end
           
    for k=n:-1:1
        for l=n:-1:1
            if C(k,l)==1 & A(k)==1
            Acol(i)=k;
            Arow(i)=l;
            i=i+1;
            end
         end
    end
Acol=unique(Acol);
Arow=unique(Arow);

number=1:1:length(CC);

for j=length(Acol):-1:1
    CC(:,Acol(j))= [];
    number(Acol(j))=[];
end

for j=length(Arow):-1:1
    CC(Arow(j),:)= [];
end


    for j=1:length(CC)   
    sumCC(j)=sum(CC(:,j));
    end
    sumCC;
    sumCCmax=sumCC(1);
    for j=1:length(sumCC)
        if sumCC(j)>=sumCCmax
            sumCCmax=sumCC(j);
            maxi=j     ;       
        end               
    end
    number(maxi);
    A(number(maxi))=1;
    
    BB=zeros(n,1);
    for j=1:n
        if A(j)==1
            BB=BB+C(:,j);
        end
    end
       
    regionsum=1;
    for j=1:n
        if BB(j)==0
            regionsum=0;
        end
    end
clear Acol Arow sumCC
end
 Acare=A;


end