n = int(6)
arr = "0 1 2 1 2 3".split()

l = len(arr)
arr = list(set(arr))
arr.sort()

zeros = 0
for i in arr: 
	if i == '0':
		zeros += 1
	else: 
		print(i, end=' ')
print('0 '*(zeros+l-len(arr)))