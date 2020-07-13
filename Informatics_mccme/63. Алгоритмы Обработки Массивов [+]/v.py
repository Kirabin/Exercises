n = int(6)
arr = list(map(int, "28 204 103 804 105 106	".split())) 
k, n = 2, 3


flag = 1
for i in arr: 
	if i%k == 0 and i%n != 0 and len(str(i)) == 3:  
		print(i, end=' ')
		flag = 0

if flag:
	print(0)