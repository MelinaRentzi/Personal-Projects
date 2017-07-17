function D=feasiator(A,C) % Function that evaluates our chromosomes
%  1------> Feasible
%  0------> Infeasible

% 1i stili to athroisma tis grammis tou xrwmoswmatos
% 2i stili an einai feasible h infeasible
n=length(C);
B=zeros(n,n);
D=ones(1,2);

for i=1:1
    for j=1:n
       if A(1,j)==1;
        B(:,i)=B(:,i)+C(:,j);
       end
    end



    for k=1:n
        if B(k,1)<1
        D(1,2)=0;
        end
    end
D(1,1)=sum(A(1,:));
% end

end