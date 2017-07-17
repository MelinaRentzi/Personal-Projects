function F= swap_line(F,i,j)
val=F(i,:);
F(i,:)=F(j,:);
F(j,:)=val;
end