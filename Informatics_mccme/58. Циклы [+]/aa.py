def is_simple(a):
	if a == 2: return 1
	if a%2 == 0: return 0 
	for i in range(3, int(a**0.5)+1, 2):
		if a%i == 0:
			return 0
	return 1 

start, end = 24, 28
flag = 1
for i in range(start, end+1): 
	if is_simple(i): 
		flag = 0
		print(i, end=' ')

if flag: 
	print(0)
