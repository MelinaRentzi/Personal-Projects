with open('f.txt', 'r', encoding = 'utf-8') as f:
    for x in range(3):
        print(f.read().split('\n')[0])
        f.seek(0)
