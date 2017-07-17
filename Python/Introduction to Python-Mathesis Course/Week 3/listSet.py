'''12.4 Να κατασκευάσετε συνάρτηση που παίρνει στην
είσοδο μια λίστα και επιστρέφει τη λίστα με μοναδικά
στοιχεία.
'''
def listSet(li):
    #epistrefei th lista xwris dipla stoixeia
    if not type(li) is list:
        return [] # elegxos oti ontws einai lista ayto p grapsame
    liNew=[]
    for i in li:
        if i not in liNew: liNew.append(i)
        liNew.sort()
    return liNew

liNew=[5,6,7,8,4,2,1,0,0,7,5,67,4,3,555,6,7,3,2,1]
print(listSet(liNew))

