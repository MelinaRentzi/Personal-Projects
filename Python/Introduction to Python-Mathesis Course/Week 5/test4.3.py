import os
count = 0
for (r,d,f) in os.walk(os.getcwd()):
    count += 1
print("a =", count)

a = 124
