% eyresh prwtvn arithmvn
close all
clear all
clc
 tic
S=2000;
N= 1:1:S;
N=N' ;
NN=5;
j=2;
while length(N)~=length(NN)
NN=N;
for i=length(N):-1:1
if rem(N(i),N(j))==0 & N(i)~=N(j)
    N=removerows(N,i);

end
end

N(j);
j=j+1;
end

toc , S , N