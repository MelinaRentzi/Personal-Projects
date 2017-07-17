clear all
close all
clc


x=1:1:13;
y=1:1:13;
z=1:1:13;

tic
megisto=1;
w=1;
for i=1:13
    for j=1:13
        for k=1:13
            if x(i)+y(j)+z(k)==15
              A(w,:)= [ w, i,j,k, x(i)*y(j)*z(k) ];
              w=w+1;
            end
        end
    end
end
toc
B=A;
A;
for i=1:length(A)
   if A(i,5)>=megisto
       megisto=A(i,5);
   end
end
megisto;

w=1;
for j=1:length(B)
ela=[1 , B(1,5)]
ii=size(B)
imax=ii(1,1)
for i=1:imax
    if B(i,5)<ela(1,2);
        ela= [ i ,B(i,5)];
    end
end
ela;

sorted(w,:) = B(ela(1,1),:);
B=removerows(B,ela(1,1));
w=w+1;

end
sorted
B
