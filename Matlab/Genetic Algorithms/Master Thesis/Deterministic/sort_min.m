function F=sort_min(F)

n=length(F);


    for j=1:(n-1)
        
        min=F(j,2);
        min_line=j;

         for i=n:-1:(j+1)
        if F(i,2)<=min
            min_line=i;
            min=F(i,2);
        end
    end
        val=F(min_line,:);
        F(min_line,:)=F(j,:);
        F(j,:)=val;
        
    end

end