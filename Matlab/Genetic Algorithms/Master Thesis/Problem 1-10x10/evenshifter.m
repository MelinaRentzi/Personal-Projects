function CCsorted=evenshifter(Csorted)

n=length(Csorted);
CCsorted=Csorted;

for i=2:2:n
        for j=1:n/2
        A(j)=Csorted(i,j+5);
        A(j+5)=Csorted(i,j);
    end
    CCsorted(i,:)=A;
end

end