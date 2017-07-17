def f():
	global a
	a = a + 1
	print(a, end = ' ')
a = 1
f()
print(a, end = ' ')
