def func(a): 
	units = map(int, str(a))

	s = 0
	for i in units: 
		s += i**3

	if s == a: 
		return 1
	return 0


start, end = 500, 600 or map(int, input().split()) 

flag = 1
for i in range(start, end+1): 
	if func(i):
		flag = 0
		print(i, end=' ')
if flag: 
	print('-1')