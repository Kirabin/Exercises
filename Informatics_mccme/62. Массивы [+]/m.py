import random 

start, end, n, k = 10, 90, 10, 8 or map(int, input().split()) 

count = 0 
for i in range(n): 
	a = random.randint(start, end)
	print(a, end=' ')
	if sum([int(i) for i in str(a)]) == k:
		count += 1

print()
print(count)