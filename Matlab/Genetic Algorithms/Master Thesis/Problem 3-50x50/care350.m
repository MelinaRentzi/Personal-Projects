%elegxos feasibility
function Ocare=care350(O1,C,O1evaluated)

n=length(C);
Ocare=zeros(n);
    for i=1:n
        if O1evaluated(i,2)==1 %an einai feasible astin opws einai
            Ocare(i,:)=O1(i,:);
        else   Ocare(i,:)=caretaker50(O1(i,:),C); %alliws trexoume ton care and share 
            
        end
    end
end