def divisors(a): 
	l = []
	for i in range(1, a//2+1): 
		if a%i == 0: 
			l.append(i)

	return l

def perfect(a, divs): 
	if sum(divs) == a:
		return 1
	return 0

inp = int(input())
divs = divisors(inp)

if perfect(inp, divs):
	print(' '.join([str(i) for i in divs]))
else: 
	print(0)
