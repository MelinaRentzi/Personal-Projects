clear all 
close all
clc



S=2000;
z=1;
zz=1;
primer=0;
tic
for i=1:S
    for j=1:i
       
        
        
    if i==1
        primer=2;
    elseif rem(i,j)==0 
        primer=primer+1;
      end
    
    
    end
    if primer==2
       Primes(zz)= i;
       zz=zz+1;
    end
    primer=0;
    
end
toc , Primes'



N=1337
primer1337=0;
for i=1:N
   if rem(N,i)==0 
       i
   primer1337=primer1337+1;
   end
end

   primer1337