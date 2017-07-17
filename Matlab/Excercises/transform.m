function A=transform(D)


[ x , y ] = size(D);
A=zeros(x,y);
    for i=1:x
        for j=1:y
            
            if D(i,j)<=70
                A(i,j)=1;
            end
        end
    end


end