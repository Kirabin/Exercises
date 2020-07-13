def is_simple(a): 
	if a == 2: return 1

	if a%2 == 0 or a == 1: 
		return 0 
	
	i = 3
	while i*i <= a: 
		if a%i == 0: return 0
		i += 2	
	return 1

n = 6
arr = list(map(int, "1 2 3 4 5 6".split()))

flag = 1
for i in arr: 
	if is_simple(i):
		print(i, end=' ')
		flag = 0

if flag: print(0)