%sortaroume ta 70 xrwmoswmata se ascending order apo to mikrotero fitness
function sorted=sort_care50(A)

AA=A;
[rows,col]=size(AA);
sorted=zeros(rows,col);
min=A(1,51);

for j=1:rows
    [row,col]=size(AA);
    min=AA(1,51);
    row;
for i=row:-1:1    
    if AA(i,51)<=min
        min=AA(i,51);
        minrow=i;
    end
end

min;
minrow;
sorted(j,:)=AA(minrow,:);
AA(minrow,:)=[];
end
        

end


