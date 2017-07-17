function min_line=score_min(F,j)

n=length(F);
min=F(j,2);
min_line=j;
    for i=(j+1):n
        if F(i,2)<=min
            min_line=i;
            min=F(i,2);
        end
    end

end