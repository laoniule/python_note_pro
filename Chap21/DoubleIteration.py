def foo(i):
	return i,i+0.5


for i in range(3):
	for x in foo(i):
		print(str(x))

