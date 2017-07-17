import myabs

while True :
    n = input('δώσε αριθμό:')
    if n == '' : break
    else : n = myabs.abs(n)
    if n: print("η απόλυτη τιμή του είναι {}".format(n))
    else: print("δεν είναι αριθμός!!!")
