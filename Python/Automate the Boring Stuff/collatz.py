def collatz(number):
    
    if number%2==0:
        print(number//2)
        return number//2
    else:
        odd = 3*number+1
        print(odd)
        return odd

n=input("Insert a number: ")
n=collatz(int(n))
while n!=1:
    n=collatz(n)
