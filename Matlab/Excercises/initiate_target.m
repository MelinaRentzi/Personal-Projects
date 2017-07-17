function F=initiate5(F)

n=length(F)
    for j=1:(n-1)
        
        imin=score2(F,j,200);
        F=swap_line(F,imin,j);
        
    end

end