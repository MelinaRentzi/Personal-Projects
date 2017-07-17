function min_line=score2(F,j,target)

n=length(F);
min=F(j,2);
min_line=j;
    for i=(j+1):n
        if abs(F(i,2)-target)<=abs(min-target)
            min_line=i;
            min=F(i,2);
        end
    end

end