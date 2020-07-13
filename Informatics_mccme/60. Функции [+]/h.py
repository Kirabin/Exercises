def is_friendly(a, b):
	if sum(divisors(a)) == b and \
	   sum(divisors(b)) == a: 
		return 1
	return 0

def divisors(a): 

	l = []
	for i in range(1,a): 
		if a%i == 0: 
			l.append(i)
	return l


a, b = 220, 284
print('YES' if is_friendly(a, b) else 'NO')