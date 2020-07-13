a, b, c, n = 2, 5, 13 ,185

l = []
ways = 0
for ka in range(n//a + 1):

	for kb in range((n-ka*a)//b + 1): 

		for kc in range((n-ka*a-kb*b)//c + 1):

			if ka*a + kb*b + kc*c == n: 
				l.append([ka, kb, kc])
				ways += 1

print(ways) 
for i in l: 
	for j in i: 
		print(j, end=' ')
	print()