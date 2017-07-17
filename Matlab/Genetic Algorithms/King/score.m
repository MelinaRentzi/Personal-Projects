function [fitness, object]=score(phen, popsize)
% This functions calculates the objective function values and the fitness values of the phenotypic population.
% 	 fitness : fitness values of the population object : objective function values of the population
% 	phen : phenotypic representation of the population popsize : population size.
for i=1:popsize
      object(i)=phen(i,1)^2+phen(i,2)^2-0.3*cos(3*pi*phen(i,1))-0.4*cos(4*pi*phen(i,2))+0.7;
      fitness(i)=1/(object(i)+1); %  Fitness 
end;   
% end score
