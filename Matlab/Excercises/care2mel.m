function Ocare=care2mel(O1,C,O1evaluated)

n=length(C);
Ocare=zeros(n);
    for i=1:1
        if O1evaluated(i,2)==1 %ean einai feasible to afinei opws einai
            Ocare(i,:)=O1(i,:);
        else   A=O1(i,:)
           ii=1;
           regionsum=0;
         
           while regionsum ~=1
               
    for k=n:-1:1
        for l=n:-1:1
            CC=C;
            if C(k,l)==1 & A(k)==1 %epilegoume poies grammes k stiles tha vgoun
            Acol(ii)=l;
            Arow(ii)=k;
            ii=ii+1;
            end
         end
    end
    
Acol=unique(Acol)
Arow=unique(Arow)

%afairoume tis grammes k stiles p epileksame parapanw
number=1:1:length(CC);

for j=length(Acol):-1:1
    CC(:,Acol(j))= [];
    number(Acol(j))=[]
end

for j=length(Arow):-1:1
    CC(Arow(j),:)= [];
end
    
    

    
    % find the maximum number of regions that can be covered 
    % by any unselected potential site
    sumCC=sum(CC);
    sumCCmax=sumCC(1);
    for j=1:length(sumCC)
        if sumCC(j)>=sumCCmax
            sumCCmax=sumCC(j)
            maxi=j            
        end
               
    end
    number(maxi)
    A(number(maxi))=1
    
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
    
        
    end
    

        end
   
    
           Ocare(i,:)=A;
         end
    end
