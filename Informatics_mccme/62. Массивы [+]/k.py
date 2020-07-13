import random 

start, end, n = 50, 200, 10 or map(int, input().split()) 

count = 0 
for i in range(n): 
	a = random.randint(start, end)
	print(a, end=' ')
	if len(str(a)) == 3:
		count += 1

print()
print(count)