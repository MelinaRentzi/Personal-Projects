function [new_gen,selected] = reproduc(old_gen,fitness)
%REPRODUC selects individuals proportional to their fitness.
%	[NEW_GEN,SELECTED] = MATE(OLD_GEN,FITNESS) selects 
%       individuals from OLD_GEN proportional to their FITNESS
%       NEW_GEN will have the same number of individuals as OLD_GEN.
%       SELECTED contains the indices (rows) of the selected
%       individuals (ie: NEW_GEN=OLD_GEN(SELECTED,:)).
%
%	Copyright (c) 1993 by the MathWorks, Inc.
%	Andrew Potvin 1-10-93.

norm_fit = fitness/sum(fitness);
selected = rand(size(fitness));
sum_fit = 0;
for i=1:length(fitness),
   sum_fit = sum_fit + norm_fit(i);
   index = find(selected<sum_fit);
   selected(index) = i*ones(size(index));
end
new_gen = old_gen(selected,:);

% end reproduc
