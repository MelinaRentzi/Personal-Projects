 function [B, Percentage]=uniqueator(A)
 [sort , ia , ic ]=unique(A,'rows');
 [a , b ]=size(ia);
 [N , M]=size(A);
 count_A=zeros(a,1);
 for i=1:a
     for j=1:N
         if ic(j)==i
             count_A(i)=count_A(i)+1;
         end        
     end
 end
 [N , M]=size(A);
 Percentage=count_A/N
 
B= horzcat(sort,count_A)

 for j=1:(a-1)
        
        max=B(j,13);
        max_line=j;

         for i=a:-1:(j+1)
        if B(i,13)>=max
            max_line=i;
            max=B(i,13);
        end
    end
        val=B(max_line,:);
        B(max_line,:)=B(j,:);
        B(j,:)=val;
        
        val=Percentage(max_line,:);
        Percentage(max_line,:)=Percentage(j,:);
        Percentage(j,:)=val; 
    end


 end