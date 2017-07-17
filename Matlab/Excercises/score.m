function min_line=score1(F,j)

n=length(F);
imin=F(1,2);
min_line=1;
    for i=(j+1):n
        if F(i,2)<=imin
            min_line=i;
        end
    end

end