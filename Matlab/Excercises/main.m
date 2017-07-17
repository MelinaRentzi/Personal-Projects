clc , close all , clear all
A= [ 1 10 ; 2 20; 3 30 ; 4 40 ; 5 50]  %5 zeygaria timwn tou dianysmatos x=(x(1),x(2))

for i=1:5
B(i,1)=Myfunction(A(i,:)); %ypologismos twn 5 diaforetikwn timwn ths Myfunction
end
B