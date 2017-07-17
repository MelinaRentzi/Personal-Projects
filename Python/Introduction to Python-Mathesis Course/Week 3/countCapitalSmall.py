'''12.3 Να κατασκευάσετε πρόγραμμα που καλεί συνάρτηση
που μετράει τα κεφαλαία και μικρά γράμματα σε μια φράση.
'''
def countCapitalSmall(s):
    countCapital=0
    countSmall=0
    for c in s:
        if c.isalpha():
            if c.lower()==c:
                countSmall+=1
            else:
                    countCapital+=1
    return countCapital, countSmall

st=input("Phrase: ")
print(countCapitalSmall(st))
