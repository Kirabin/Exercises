a = '5221' or input()

flag = 0
for i in range(len(a)):
	if a[i] == a[i-1]:
		flag = 1

if flag: 
	print('YES')
else: 
	print('NO')
