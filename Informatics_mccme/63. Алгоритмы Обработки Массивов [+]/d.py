n = 6
arr = map(int, "1 2 3 1 5 2".split())

min_count = 0
min_number = 10000
for i in arr:
	if i == min_number: 
		min_count += 1
	elif i < min_number: 
		min_number = i 
		min_count = 1
print(min_number, min_count)