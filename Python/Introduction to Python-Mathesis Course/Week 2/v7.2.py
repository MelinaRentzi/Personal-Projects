a = input("α=")
b = input("β=")
c = input("γ=")
print ("Θα λύσουμε την εξίσωση: ")
print ("{}x**2 + {}x + {} = 0\n".format(a,b,c))
a = float(a)
b = float(b)
c = float(c)

if a == 0 :
    if b == 0 :
        if c == 0 :
            print("Υπάρχουν άπειρες λύσεις")
        else :
            print("Δεν υπάρχουν λύσεις")
    else :
        print ("Οι λύσεις είναι χ1 = χ2 = {:1.2f}".format( - c/b ))
else :
    diak = b**2 - 4 * a * c
    print("H διακρίνουσα είναι {:1.2f}".format(diak))

    if diak < 0 :
        print("Η εξίσωση δεν έχει πραγματικές λύσεις")
    else :
        x1 = (-b + diak**0.5)/(2*a)
        x2 = (-b - diak**0.5)/(2*a)
        print("Οι λύσεις είναι: χ1 = {:1.2f}, χ2 = {:1.2f}".format(x1,x2))
