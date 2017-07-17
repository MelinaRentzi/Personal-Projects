with open('f.txt', 'r', encoding='utf-8') as f:
    x = f.read()
    with open('f2.txt', 'w', encoding='utf-8') as f1:
        f1.write(x)
