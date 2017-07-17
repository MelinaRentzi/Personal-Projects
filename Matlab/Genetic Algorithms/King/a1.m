% 28/6/2016   eftiaksa ena neo pinaka E2 me diaforetiko tropo kanontas
% xrhsh i,j kai if


clear all
close all
clc

% A (4X4) me ola ta stoixeia toy 1
A=ones(4)

% to 2,4 stoixeio na ginei 8
A(2,4)=8

%olh h deyteri stili na ginei 3
A(:,2)=3

% pinakas B ;ola ta stoixeia 3 ,ektos apo thn diagwnio poy einai 5
n=10
B=3*ones(n)
for i=1:n
B(i,i)=5;
end
B

% C 30X4    
%1 sthlh o arithmos ths grammhs
tic
n=1500;
% preallocation
C=zeros(n,4);
for i=1:n
    C(i,1)=i;
    C(i,2)=i^2;
    C(i,3)=sin(i);
    C(i,4)=C(i,1)+C(i,2)+C(i,3);
end
C;
a=toc

% D pantoy 2 diagwnios 1
n=4;
D=2*ones(n);
for i=1:n
D(i,i)=1;
end
D


%E=  [ 1 2 1 1
%      2 1 2 1
%      1 2 1 2
%      1 1 2 1 ]

E=ones(n);
for i=1:n-1
E(i+1,i)=2;
E(i,i+1)=2;
end
E

E2=ones(n);
for i=1:n
    for j=1:n
      if  abs(i-j)==1
          E2(i,j)=2;
      end
    end
end
      E2


%F=  [ 1 0 -1  0
%      0 1  0 -1
%      1 0 -1  0
%      0 1  0 -1 ]

F=zeros(4);
for i=1:2
    F(i,i)=1;
    F(i+2,i)=1;
    F(i,i+2)=-1;
    F(i+2,i+2)=-1;
end
F




 
 F2=zeros(n);
for i=1:n
    for j=1:n
   if i==j        
       F2(i,j)=2;
   else
       F2(i,j)=3;
   end
    end
end
 F2



 F3=zeros(n);
 for i=1:n
    for j=1:n
   
        if mod(i+j,2)==0
            F3(i,j)=1;
        end
        
        if j>=3
            F3(i,j)=-F3(i,j);
        end
        
        
    end
end
F3

 F4=zeros(n);
for i=1:n
    for j=1:n
   if mod(i+j,2)==0     && j>=3   
       F4(i,j)=-1;
   elseif mod(i+j,2)==0 && j<=2
       F4(i,j)=1;
   end
    end
end
 F4
