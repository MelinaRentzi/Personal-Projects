%sortaroume ta 70 xrwmoswmata se ascending order apo to mikrotero fitness
function sorted=sort_care(A)

AA=A;
[rows,col]=size(AA);
sorted=zeros(rows,col);
min=A(1,11);

for j=1:rows
    [row,col]=size(AA);
    min=AA(1,11);
    row;
for i=row:-1:1    
    if AA(i,11)<=min
        min=AA(i,11);
        minrow=i;
    end
end

min;
minrow;
sorted(j,:)=AA(minrow,:);
AA(minrow,:)=[];
end
        

end


