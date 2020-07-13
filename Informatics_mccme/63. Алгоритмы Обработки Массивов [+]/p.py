n = int(6)
arr = "1 0 2 0 3 4".split()

zeros = 0
for i in arr: 
	if i == '0':
		zeros+= 1
	else: 
		print(i, end=' ')
print('0 '*zeros)