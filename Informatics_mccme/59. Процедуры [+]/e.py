def print_divisors(a): #dividers
	for i in range(1,a+1): 
		if a%i == 0:
			print(i, end=' ')


a = 1245
print_divisors(a)
