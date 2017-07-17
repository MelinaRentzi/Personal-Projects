clear all
clc


MaxDistance=300 ; % mexri poion arithmo tha pairnei times
X=10 ; % diastash pinaka (X,X)
Y=70 ; % orio    C<Y


C=distance(MaxDistance,X,Y);

for M=1:10
F=zeros(length(C),2);
F(:,1)= 1:1:length(C);
F(:,2)=sum(C); %Number of 1s

F=sort_min(F); %Number of 1s ascending order and rearranged rows of covering coefficient

Csorted=Csorter(F,C);


[ O1, O2 ,O3, O4 , O5 , O6 , O7 ]=operators(Csorted); % "Crossover operation" (reproduction), all 7 operators

%Oi O(i)evaluated einai pinakes me prwth sthlh to fitness k deyterh stili
%to feasible/infeasible
O1evaluated=feasiator(O1,Csorted);
O2evaluated=feasiator(O2,Csorted);
O3evaluated=feasiator(O3,Csorted);
O4evaluated=feasiator(O4,Csorted);
O5evaluated=feasiator(O5,Csorted);
O6evaluated=feasiator(O6,Csorted);
O7evaluated=feasiator(O7,Csorted); 

% horzcat = i entoli pou vazei ta xrwmoswmata, to fitness kai to feasible
% infeasible ston idio pinaka opws sto vivlio
O1full=horzcat(O1,O1evaluated);
O2full=horzcat(O2,O2evaluated);
O3full=horzcat(O3,O3evaluated);
O4full=horzcat(O4,O4evaluated);
O5full=horzcat(O5,O5evaluated);
O6full=horzcat(O6,O6evaluated);
O7full=horzcat(O7,O7evaluated);


 O1care=care3(O1,C,O1evaluated); %elegxos k efarmogh tou care and share algorithm
 O1eva=feasiator(O1care,C); %elegxoume an egine feasible (pou egine) kai o O1eva einai 2 sthles, sthn prwth to fitness sthn deyterh monades
 O1carefull=horzcat(O1care,O1eva); %o pinakas me ta diorthwmena xrwmoswmata kai ta fitness tous
 
 O2care=care3(O2,C,O2evaluated);
 O2eva=feasiator(O2care,C);
 O2carefull=horzcat(O2care,O2eva);
 
 O3care=care3(O3,C,O3evaluated);
 O3eva=feasiator(O3care,C);
 O3carefull=horzcat(O3care,O3eva);
 
 O4care=care3(O4,C,O4evaluated);
 O4eva=feasiator(O4care,C);
 O4carefull=horzcat(O4care,O4eva);
 
 O5care=care3(O5,C,O5evaluated);
 O5eva=feasiator(O5care,C);
 O5carefull=horzcat(O5care,O5eva);
 
 O6care=care3(O6,C,O6evaluated);
 O6eva=feasiator(O6care,C);
 O6carefull=horzcat(O6care,O6eva);
 
 O7care=care3(O7,C,O7evaluated);
 O7eva=feasiator(O7care,C);
 O7carefull=horzcat(O7care,O7eva);
 
 
 
TaPantaOla=vertcat(O1carefull,O2carefull,O3carefull,O4carefull,O5carefull,O6carefull,O7carefull); %kai ta 70 xrwmoswmata

TaPantaOlaSorted=sort_care(TaPantaOla); %kai ta 70 xrwmoswmata sortarismena

Csorted=TaPantaOlaSorted(1:10,1:10); %epilegoume ta 10 prwta gia thn epomenh epanalhpsh
A(M,:)=TaPantaOlaSorted(1,:); %to prwto xrwmoswma tou teleytaiou pinaka einai to veltisto (olh h prwth grammh)
end
disp('H veltisth lysh einai=');disp(TaPantaOlaSorted(1,:));
% end %edw trexei 1000 fores o algorithmos

% [B ,C]=uniqueator(A); %%function pou afotou exei treksei o algorithmos 1000 fores,
%metraei to pososto emfanishs kathe xrwmoswmatos san veltisth lysh