def is_fib(num): 
	a = 1; b = 1 
	while b < num: 
		a, b = b, a+b

	if b == num:
		return 1
	return 0

n = 6
arr = list(map(int, "4 14 5 8 12 13".split())) 

flag = 1
for i in arr: 
	if is_fib(i):
		print(i, end=' ')
		flag = 0
if flag:
	print(0)