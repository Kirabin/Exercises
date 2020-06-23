# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):

	a = integers[0]
	b = integers[1]
	i = 2
	while 1: 
		if a % 2 == b % 2:
			outlier = (a+1) % 2
			break
		
		a = b
		try: 
			b = integers[i]
		except: 
			b = integers[0]
		i += 1



	for i in integers: 
		if i % 2 == outlier: 
			return i

	return -1


assert find_outlier([0, 1, 2]) == 1
assert find_outlier([2, 4, 6, 8, 10, 3]) == 3
assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160