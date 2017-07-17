# Μάθημα 19: Regular Expressions
# 19.2 Παράδειγμα: Ψάχνουμε παραμύθια
import re
tonoi = ('αά', 'εέ', 'ηή', 'ιί', 'οό', 'ύυ', 'ωώ')
tw = 'Trivizas_works.txt'
try:
    with open(tw, 'r', encoding = 'utf-8') as f:
        works = f.read()
    for line in works.split('\n'):
        print(line)
except IOError as e:
    print(e)
while True:
    phrase = input('Δώσε λέξη-κλειδί:')
    if phrase == '': break
    n_phrase = ''
    for c in phrase:
        char = c
        for t in tonoi:
            if c in t: char = '['+t+']'
        n_phrase += char
    print(n_phrase)
    pattern = '.*'+n_phrase+'.*'
    w =re.findall(pattern, works, re.I)
    for work in w:
        print(work)
