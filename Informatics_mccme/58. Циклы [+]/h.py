def func(a): 
	units = map(int, str(a))
	for i in units: 
		if i == 0:
			return 0
		if a%i != 0:
			return 0
	return 1 

start, end = 10, 100 or map(int, input().split()) 

for i in range(start, end+1): 
	if func(i):
		print(i, end=' ')