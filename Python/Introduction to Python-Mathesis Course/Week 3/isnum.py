'''Να κατασκευάσετε συνάρτηση isnum()
που δέχεται στην είσοδο μια συμβολοσειρά και
απαντάει αν είναι αποδεκτός αριθμός ή όχι.
-123.45
'''
def isnum(n):
    #Synarthsh p vriskei an mia symvoloseira einai arithmos
    if not type(n) is str:
        return False
    n=n.strip() #afairoume ta kena
    if n.isdigit():
        return True
    elif n[0] in '+-' and isnum(n[1:]): #to prwto stoixeio einai + h - k apo ekei k pera arithmos
        return True
    elif "." in n:
        if n.count(".")==1 and isnum(n.replace(".","")):
            return True
        else:
            return False
    else:
        return False
while True:
        n=input("n=")
        if n =="": break
        print(isnum(n)) #edw testaroume an ontws ta kanei swsta
