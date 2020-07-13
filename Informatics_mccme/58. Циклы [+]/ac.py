#works very long

def divisors(a): 
	l = []
	for i in range(1, a): 
		if a%i == 0: 
			l.append(i)

	return l


def is_perfect(a): 
	if sum(divisors(a)) == a:
		return 1
	return 0


inp = 100
flag = 1
for i in range(2, inp):
	if is_perfect(i):
		print(i, end=' ')
		flag = 0
if flag: 
	print(0)