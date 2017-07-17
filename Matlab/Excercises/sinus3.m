for i=10:-1:1
   i-9 
end

t=linspace(0,pi);

for i=1:8
    
    figure(i)
    plot(t,sin(i*t))
%     strcat('y',num2str(i))  %=sin(i*t);
    
    figure(11)
    plot(t,sin(i*t)+2*i)
    hold on
end
    