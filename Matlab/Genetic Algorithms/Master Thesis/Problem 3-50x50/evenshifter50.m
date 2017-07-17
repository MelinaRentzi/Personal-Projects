function CCsorted=evenshifter50(Csorted)

n=length(Csorted);
CCsorted=Csorted;

for i=2:2:n
        for j=1:n/2
        A(j)=Csorted(i,j+25);
        A(j+25)=Csorted(i,j);
    end
    CCsorted(i,:)=A;
end

end