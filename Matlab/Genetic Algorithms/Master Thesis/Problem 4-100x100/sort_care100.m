%sortaroume ta 70 xrwmoswmata se ascending order apo to mikrotero fitness
function sorted=sort_care100(A)

AA=A;
[rows,col]=size(AA);
sorted=zeros(rows,col);
min=A(1,101);

for j=1:rows
    [row,col]=size(AA);
    min=AA(1,101);
    row;
for i=row:-1:1    
    if AA(i,101)<=min
        min=AA(i,101);
        minrow=i;
    end
end

min;
minrow;
sorted(j,:)=AA(minrow,:);
AA(minrow,:)=[];
end
        

end


