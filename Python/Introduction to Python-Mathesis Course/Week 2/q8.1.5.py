d = {1: 'h', 2: 'e', 3: 'l', 4: 'l', 5: 'o'}
for i in sorted(d, key =d.get):
	print(d[i],end='')
else: print('world')
