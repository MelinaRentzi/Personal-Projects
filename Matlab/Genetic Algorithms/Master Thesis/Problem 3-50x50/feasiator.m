function D=feasiator(A,C) % Function tha evaluates our chromosomes
%  1------> Feasible
%  0------> Infeasible

% 1i stili to athroisma tis grammis tou xrwmoswmatos
% 2i stili an einai feasible h infeasible
n=length(C);
B=zeros(n,n);
D=ones(n,2);

for i=1:n
    for j=1:n
       if A(i,j)==1;
        B(:,i)=B(:,i)+C(:,j);
       end
    end



    for k=1:n
        if B(k,i)<1
        D(i,2)=0;
        end
    end
D(i,1)=sum(A(i,:));
end

end