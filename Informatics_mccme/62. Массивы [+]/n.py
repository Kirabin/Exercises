import random 

start, end, n = -20, 4, 10 or map(int, input().split()) 

max_num = -1 
for i in range(n):
	a = random.randint(start, end)
	print(a, end=' ')
	if a%2==0 and a>0 and a>max_num:
		max_num = a

print()
print(max_num)