n = int(6) 
arr = list(map(int, "4 1 2 1 2 3".split())) 

d = {}
for i in arr: 
	if d.get(i):
		d[i] += 1
	else: 
		d[i] = 1

for key, value in d.items(): 
	if value > 1: 
		print(key, end=' ')