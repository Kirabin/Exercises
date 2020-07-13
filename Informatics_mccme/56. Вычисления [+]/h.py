import random 

start, end = 1.234, 2.34

for i in range(5):
	a = end 
	while a == end: 
		a = random.uniform(start, end)
	print(F"{a:.3f}", end=' ')

