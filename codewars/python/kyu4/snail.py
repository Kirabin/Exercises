# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

def snail(snail_map):
	i, j = 0, -1
	
	n = len(snail_map[0])
	res = []

	for k in range(0, n//2):
		while j < n-1-k: 
			j += 1
			res.append(snail_map[i][j])

		while i < n-1-k: 
			i += 1
			res.append(snail_map[i][j])	

		while j > 0+k:
			j -= 1
			res.append(snail_map[i][j])

		while i > 0+1+k:
			i -= 1
			res.append(snail_map[i][j])

	if n % 2 == 1:
		res.append(snail_map[n//2][n//2])

	return res


assert snail([[]]) == []

array = [[1,2,3],
		 [8,9,4],
		 [7,6,5]]

expected = [1,2,3,4,5,6,7,8,9]

assert snail(array) == expected

array = [[1,2,3,4],
		 [12,13,14,5],
		 [11,16,15,6],
		 [10,9,8,7]]

expected = list(range(1,17))

assert snail(array) == expected
