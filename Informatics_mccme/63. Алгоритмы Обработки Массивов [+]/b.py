n = 6
arr = map(int, "1 2 3 2 5 2".split())
k = 2 

count = 1
for i in arr: 
	if i == k: 
		print(count)
	count += 1
