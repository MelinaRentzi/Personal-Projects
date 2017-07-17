import os
import os.path
s = 0
for (r,d,f) in os.walk('.'):
    for fi in f: 
        fs = os.path.getsize(os.path.join(r,fi))
        if  fs > s: s = fs
print('{:1.2f}'.format(s/1024**3))
