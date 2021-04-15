def max_sequence(arr):
	res = 0

	temp = 0
	for i in arr: 
		temp += i		
		temp = 0 if temp < 0 else temp
		res = max(res, temp)


	return res



assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6