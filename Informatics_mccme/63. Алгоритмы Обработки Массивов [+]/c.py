n = 6
arr = map(int, "1 2 3 5 5 2".split())

max_count = 0
max_number = 0
for i in arr:
	if i == max_number: 
		max_count += 1
	elif i > max_number: 
		max_number = i 
		max_count = 1
print(max_number, max_count)