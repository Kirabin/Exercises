n = 6
arr = map(int, "1 2 3 1 5 2".split())

min_number = 10000
max_number = 0 
flag = 1
for i in arr:
	if i < 0 or i%2 != 0: 
		continue
	if i > max_number : 
		max_number = i	
		flag = 0
	if i < min_number: 
		min_number = i 
		flag = 0

if flag: 
	print(-1)
else: 
	print(min_number, max_number)