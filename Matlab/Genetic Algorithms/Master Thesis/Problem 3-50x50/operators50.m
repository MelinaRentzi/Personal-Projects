function  [ O1 , O2 ,O3 , O4, O5 , O6 , O7 ]= operators50(C)

n=length(C);

% 1 Operator for Offsprings Using Logic OR and Logic AND
for i=1:n/2
    
    p=C(2*i-1,:);
    q=C(2*i,:);
    
    O1(i,:)= p | q;
    O1(i+25,:)= p & q;
   
end

% 2 Operator for Odd shift before Logic OR and Logic AND
C2=oddshifter50(C);
for i=1:n/2
    
    p=C2(2*i-1,:);
    q=C2(2*i,:);
    
    O2(i,:)= p | q;
    O2(i+25,:)= p & q;
   
end
% % 3 Operator for evenshiftbefore Logic OR and Logic AND
C3=evenshifter50(C);
for i=1:n/2
    
    p=C3(2*i-1,:);
    q=C3(2*i,:);
    
    O3(i,:)= p | q;
    O3(i+25,:)= p & q;
   
end
 
 
% % 4 Operator for Offsprings Using Logic OR and oddshift before Logic OR

for i=1:n/2
    O4(i,:)=O1(i,:);
    O4(i+25,:)=O2(i,:);
end


% % 5 Operator for Offsprings Using Logic OR and evenshift before Logic OR

for i=1:n/2
    O5(i,:)=O1(i,:);
    O5(i+25,:)=O3(i,:);
end
% % 6 Operator for Offsprings Using Logic AND and oddshift before Logic AND
for i=1:n/2
    O6(i,:)=O1(i+25,:);
    O6(i+25,:)=O2(i+25,:);
end
% %  7 Operator for Offsprings Using Logic AND and evenshift before Logic AND
for i=1:n/2
    O7(i,:)=O1(i+25,:);
    O7(i+25,:)=O3(i+25,:);
end