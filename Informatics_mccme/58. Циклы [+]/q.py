inp = 1025 or int(input()) 
count = 0
while inp: 
	inp //= 2
	count += 1



arr = [str(2**i) for i in range(2, count, 2)]
print(' '.join(arr[::-1]))