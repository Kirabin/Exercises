n = int(5) 
arr = list(map(int, "1 2 3 -2".split()))

minus_arr = []
for i in arr: 
	if i < 0: 
		minus_arr.append(i)

if minus_arr: 
	for i in minus_arr:
		print(i, end=' ')
else:
	print(0)