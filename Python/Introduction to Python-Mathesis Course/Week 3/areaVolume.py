'''12.3 Να κατασκευάσετε πρόγραμμα που ζητάει
διαδοχικά από τον χρήστη την ακτίνα σφαίρας
και υπολογίζει, καλώντας σχετικές συναρτήσεις
την επιφάνεια και τον όγκο της.
Τερματίζει με stop.
e = 4*pi*r**2
v = (4/3)*pi*r**3
'''
import math
pi=3.14
pi=math.pi
def area(r):
    return 4*pi*r**2

def vol(r):
    return (4/3)*pi*r**3

def isnum(n):
    #Synarthsh p vriskei an mia symvoloseira einai arithmos
    if not type(n) is str:
        return False
    n=n.strip() #afairoume ta kena
    if n.isdigit():
        return True
    elif n[0] in '+' and isnum(n[1:]): #to prwto stoixeio einai + h - k apo ekei k pera arithmos
        return True
    elif n[0] in '-' and isnum(n[1:]):
        return False
    elif "." in n:
        if n.count(".")==1 and isnum(n.replace(".","")):
            return True
        else:
            return False
    else:
        return False
while True:
        r=input("R=")
        if r =="stop": break
        if isnum(r):
            v=vol(float(r))
            e=area(float(r))
            print("Epifaneia = {:1.2f}, Ogos ={:1.2f}".format(e,v))
        else:
            continue #sthn periptwsh p dn einai arithmos ksanarwta gia to r
