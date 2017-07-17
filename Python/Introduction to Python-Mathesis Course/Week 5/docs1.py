# Μάθημα 18.2:  Παρουσίαση των αρχείων μας (Παράδειγμα από το video)

'''
Να παρουσιάστε με κατάλληλη στοίχιση την ιεραρχία του συστήματος
αρχείων του υπολογιστή σας.
'''
import os
import os.path

while True:
    dir =input('Αρχικός φάκελος:')
    if dir == '': break
    if os.path.isdir(dir):
        count_files = 0
        for r,d,f in os.walk(dir):
            level = r.replace(dir, '').count(os.sep)
            print(level*'\t',r)
            for fi in f:
                if fi[0] not in '.~':
                    print((level+1)*'\t',fi)
                    count_files += 1
    print('βρέθηκαν {} αρχεία'.format(count_files))    
