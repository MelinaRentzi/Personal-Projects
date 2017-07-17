def func(*a):
	return sum([x for x in a if x%2 == 0])
print(func(2, 3, 4, 5))
