%Rearrange the Covering Coefficient Matrix in ascended order of their fitness function

function Csort=Csorter(F,C)
n=length(F);
for i=1:n
        Csort(i,:)=C(F(i,1),:);
end
    