import random 

start, end, n = 10, 20, 5 or map(int, input().split()) 
for i in range(n):
	print(random.randint(start, end), end=' ')