def is_simple(a):
        if a == 1:
                return 0
        if a%2 == 0:
                return 0 
	
	i = 3
        while i*i <= a: 
		if a%i == 0: return 0
		i += 2
	return 1

start, stop = 1, 10000

flag = 1
for k in range(start, stop): 
	for i in range(len(str(k))): 
		if not is_simple(k//(10**i)):
			break
	else: 
		print(k, end='\n')
		flag = 0

if flag:
	print(0)
