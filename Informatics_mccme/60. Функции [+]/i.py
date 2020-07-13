# Works very long

import time
start_time = time.time()

def divisors(a): 
	l = []
	for i in range(1,a): 
		if a%i == 0: 
			l.append(i)
	return l

start, stop = 1, 12000

i = start
while i <= stop:
	a = i 
	b = sum(divisors(a))

	if sum(divisors(b)) == a and a < b: 
		print(F"({a}, {b})", )
		i = b
	i += 1 

print("--- %s seconds ---" % (time.time() - start_time))