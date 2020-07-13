n = 13 or int(input())
a = 1
b = 1 
if n == 1: 
	print('1')
else: 
	print('1 1', end=' ')
	for i in range(2,n): 
		a, b = b, a+b
		print(b, end=' ')