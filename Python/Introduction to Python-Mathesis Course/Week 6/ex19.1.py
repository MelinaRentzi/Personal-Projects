# Μάθημα 19: Regular Expressions
import re
f = open('greece.txt', 'r', encoding = 'utf-8')
greece = f.read()
# Αντιακτάσταση re.sub()
print(re.sub(r'\bΕλλάδα\b', 'ΕΛΛΑΔΑ', greece))

# Εύρεση re.findall() των λέξεων που αρχίζουν από φωνήεν
print("\nΛέξεις από φωνήεντα")
pattern = r"\b[αάεέηήιίοόυύωώ][\w]*" # raw string r"..." χωρίς \
print(re.findall(pattern, greece, re.I))

f.close()
