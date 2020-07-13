import random 

start, end, n = 100, 200, 7 or map(int, input().split())

num_sum = 0
for i in range(n):
	a = random.randint(start, end)
	num_sum += a
	print(a, end=' ')

print()
print("%.3f" % (num_sum/n))