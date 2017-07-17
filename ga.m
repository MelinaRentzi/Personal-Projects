close all
clear
clc
% Main_Program ga.m

popsize=10; % Population size
maxgen=50; % Number of generations (iterations)
length=12; % Length of genotype (i.e. number of bits in the binary array)
pcross=0.8; % Probability of crossover
pm=0.01; % Probability of mutation
bits=[length length]; % Array of unknown parameters
 % Array of unknown parameters

% Array of the concatenated genotype

vlb=[-1 -1];  % Array of lowest values of the fitness function 
vub=[1 1];  % Array of highest values of the fitness function
phen=init(vlb,vub,popsize,2); % Initialization of the	population of phenotypes
[gen,lchrom,coarse,nround]=encode1(phen,vlb,vub,bits); % Conversion of phenotypes to binary string 
[fitness,object]=score(phen,popsize);% Evaluation of the fitness function 	
x=-1:0.1:1; 
y=-1:0.1:1;
[x1,y1]=meshgrid(x,y); 
z= x1^2+y1^2-0.3*cos(3*pi*x1)-0.4*cos(4*pi*y1)+0.7;  %  Evaluation of the objective	function
figure(1); % Display of fitness function
contour(x,y,z);% 3-D contour plot
[best_obj(1), index] = min(object);
best_gen=gen(index,:);
best_phen=phen(index, :); % Best initial population
[worst_obj(1), index1] = max(object);
worst_cur_gen=gen(index1);
worst_cur_phen=phen(index1); % Worst initial population
avg_obj(1)=0;
for k=1:popsize
    avg_obj(1)=avg_obj(1)+object(k);
end;
avg_obj(1)=avg_obj(1)/popsize; % Mean value of fitness
best_x(1)=best_phen(1);
best_y(1)=best_phen(2); % Best phenotype
for i1=1:2
    fprintf(1,'%f  ',best_phen(1))
end 
fprintf('\n')
fprintf(1,'BEST : %f WORST : %f AVG : %f \n', best_obj(1),worst_obj(1),avg_obj(1))  
for i=1:maxgen  % Start of algorithm
      %gen=reproduc(gen,fitness);  % Reproduction
      %gen=mate(gen); % Mate two members of the population
      gen=xover(gen, pcross) % Crossover operation
      %gen=mutate(gen, pm);    % Mutation operation
      [phen, coa] = decode1(gen,vlb,vub,bits)    	% Code phenotype 
      [fitness, object]=score(phen,popsize)   		%  Compute fitness      
      [best_cur_obj, index] = min(object)
      best_cur_gen=gen(index, :)
      best_cur_phen=phen(index, :)  	% Compute and store best solution
      [worst_obj(i+1), index1] = max(object)
      worst_cur_gen=gen(index1)
      worst_cur_phen=phen(index1)	% Compute worst solution	
	   avg_obj(i+1)=0
      for k=1:popsize
         avg_obj(i+1)=avg_obj(i+1)+object(k);
      end;
      avg_obj(i+1)=avg_obj(i+1)/popsize;	 	% Compute average value of objective function
	  if(best_cur_obj > best_obj(i)) % Apply elitist strategy
         phen(index1,:) = best_phen;
         gen(index1,:) = best_gen;
         object(index1) = best_obj(i);
         best_obj(i+1) = best_obj(i);
      elseif(best_cur_obj <= best_obj(i))
         best_phen = best_cur_phen
         best_gen = best_cur_gen;
         best_obj(i+1) = best_cur_obj;
      end;
      best_x(i+1)=best_phen(1);
      best_y(i+1)=best_phen(2);
      hold;
      line(best_x,best_y);
		% Display evolution of best solution
      for i1=1:2
         fprintf(1,'%f  ',best_phen(i1));
      end; 
      fprintf(1,'---> %f\n',best_obj(i+1));  
      fprintf('\n'); 
      fprintf(1,'BEST : %f WORST : %f AVG : %f \n', 	best_obj(i+1),worst_obj(i+1),avg_obj(i+1));  
   end;
xx=1:maxgen+1; 
figure,plot(xx,best_obj,xx,worst_obj,xx,avg_obj);
grid;
	% Display evolution of objective functions for the worst, average and 	best solutions 
%clear;
% end  Main_Program
