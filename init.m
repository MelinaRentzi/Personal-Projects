%This function creates a random population
% syntax: phen=init(vlb,vub,siz,sea)
% where phen an array with siz rows and sea columns
% sea : Number of the genes i.e. number of parameters to be searched
% vlb : a vector of lentgh sea with the lower limits of the parameters to be searched
% vub : a vector of lentgh sea with the upper limits of the parameters to be searched
% siz : The size of the population

% Athens February 1996
% Copyright : Vassilis Goggos 
% email : vasgog@ee.upatras.gr

function phen=init(vlb,vub, siz, sea)
phen=[]
for i=1:siz
    phen(i,:)=(vub-vlb).*rand(1, sea) + vlb
end