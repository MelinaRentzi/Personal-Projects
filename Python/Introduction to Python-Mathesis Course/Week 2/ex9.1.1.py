num = 0
while num > 99 or num < 10 :
    num = int(input("δώσε θετικό διψήφιο αριθμό:"))
else :
    print("ευχαριστώ, έδωσες το {:2d}".format(num))
