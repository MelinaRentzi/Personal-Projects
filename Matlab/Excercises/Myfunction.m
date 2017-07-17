function y=Myfunction(x) %otan kalw to x sto main programma prepei na to valw sth morfh poy einai, dhladh edw einai ena dianysma x=(x(1),x(2))
c=1; %sto y ginontai oi ypologismoi
y = (1/20)*(-20*exp(1)   *(-0.2*sqrt((1/2)*(x(1)^2+x(2)^2)))-...
    -exp(1)*(1/2*(cos(c*x(1))+cos(c*x(2))))+...
    +20+exp(1)+5.7);

end