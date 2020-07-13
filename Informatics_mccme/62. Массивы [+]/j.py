import random 
start, end, n = 100, 150, 5 or map(int, input().split()) 
count = 0
for i in range(n): 
	a = random.randint(start, end)
	print(a, end=' ')
	if a//10%10%2 == 0: 
		count += 1

print()
print(count)