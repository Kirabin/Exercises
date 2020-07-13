def func(a): 
	if str(a*a)[-len(str(a)):] == str(a):
		return 1 
	return 0


start, end = 20, 10000 or map(int, input().split()) 

flag = 1
for i in range(start, end+1): 
	if func(i):
		flag = 0
		print(i, end=' ')
if flag: 
	print('-1')