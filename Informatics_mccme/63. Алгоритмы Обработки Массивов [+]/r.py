n = int(6)
arr = list(map(int,"1 0 -3 2 0 3 -1 -2".split()))

zeros = 0
for i in arr: 
	if i == 0: zeros += 1

minus_arr = []
for i in arr: 
	if i < 0: minus_arr.append(i)

plus_arr = []
for i in arr: 
	if i > 0: plus_arr.append(i) 


# minus -> zeros -> plus 
for i in plus_arr: print(i, end=' ')
for i in range(zeros): print(0, end=' ')
for i in minus_arr: print(i, end=' ')

