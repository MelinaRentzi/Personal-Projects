def f():
	global a
	a = a + 7
	print(a, end = ' ')
a = 5
f()
print(a, end = ' ')
