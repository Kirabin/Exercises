def max_sequence(arr):
	res = 0

	temp = 0
	for i in arr: 
		if temp + i > 0: 
			temp += i
		else:
			temp = 0

		if temp > res:
			res = temp

	return res



assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6