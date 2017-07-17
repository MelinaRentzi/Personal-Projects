clear all
clc
CCCC=[1 0 0 0 0 0 0 1 0 0;0 1 0 0 1 0 1 0 1 0;0 0 1 0 0 1 0 0 0 1;0 0 0 1 0 0 0 0 0 0;0 1 0 0 1 0 0 0 0 0;0 0 1 0 0 1 1 0 1 1;0 1 0 0 0 1 1 0 1 1;1 0 0 0 0 0 0 1 0 0;0 1 0 0 0 1 1 0 1 0;0 0 1 0 0 1 1 0 0 1]
A=zeros(1,10);
% for i=1:6
%     A(1,i)=1;
%     
%     %D(i)=feasiator(A)
%     A=zeros(1,6);
%     
% end
% 
% 
% 
% 
% for i=1:6
%     A=zeros(1,6);
%     A(1,i)=1;
%     for j=i+1:6
%         
%         A(1,j)=1;
%         A=zeros(1,6);
%         A(1,i)=1;
%     end
% end



for i=1:10
    i ;
    A(1,i)=1; %edw ;
    D=feasiator(A,CCCC);
    
    A=zeros(1,10);
    
    for j=i+1:10
        j;
        A(1,i)=1;
        A(1,j)=1; %edw ;
        F=feasiator(A,CCCC);
        
        A=zeros(1,10);
        
        
        for k=j+1:10
            k;
            A(1,i)=1;
            A(1,j)=1;
            A(1,k)=1; %edw ;
            G=feasiator(A,CCCC);
            
            A=zeros(1,10);
        for l=k+1:10
            l;
            A(1,i)=1;
            A(1,j)=1;
            A(1,k)=1;
            A(1,l)=1
            H=feasiator(A,CCCC)
            
            A=zeros(1,10);
        end
           
        end
       
    end
   
end