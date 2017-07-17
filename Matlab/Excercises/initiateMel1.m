function F=initiateMel1(F)


D= [0        244        140        128        281        196        181        51        248        167;
244        0        158        359        37        111        66        268        60        112;
140        158        0        202        194        56        92        170        117        46;
128        359        202        0        395        258        294        179        319        248;
281        57        194        395        0        145        102        305        92        148;
196        111        56        258        145        0        60        229        61        34;
181        66        92        294        102        60        0        208        67        47;
51        268        170        179        305        229        208        0        275        195;
248        60        117        319        92        61        67        275        0        87;
167        112        46        248        148        34        47        195        87        0]  %distance matrix

A=D<70

n=length(A);
F=zeros(n,2);
for i=1:n
    F(i,1)=i;
    F(i,2)=sum(A(i,:));
    
end
initialF=F;
F

for j=1:(n-1)
    imin=j;
    for i=(j+1):n
        if F(i,2)<=F(imin,2)
            imin=i;
        end
    end
    if (imin~=j)
       
        F=swap(F,imin,j);
        F=swap1(F,imin,j);
    end
end

end