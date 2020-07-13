n = int(input())
arr = list(map(int, input().split())) 
count = int(input()) 

d = {}
for i in arr: 
	if i in d: 
		d[i] += 1
	else: 
		d[i] = 1

for k, v in d.items(): 
	if v == count: 
		print(k, end=' ')

print()