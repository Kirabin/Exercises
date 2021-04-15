# https://www.codewars.com/kata/536a155256eb459b8700077e/solutions/python

def create_spiral(size):

	if type(size) != int or size < 1:
		return []

	spiral = [[0 for j in range(size)] for i in range(size)]
	offset = 0
	i, j = 0, -1

	count = 1
	while offset <= size // 2:
		while j < size - offset - 1:
			j += 1
			spiral[i][j] = count
			count += 1

		while i < size - offset - 1:
			i += 1
			spiral[i][j] = count
			count += 1

		while j > 0 + offset:
			j -= 1
			spiral[i][j] = count
			count += 1

		offset += 1
		while i > 0 + offset:
			i -= 1
			spiral[i][j] = count 
			count += 1
		

	print(*spiral, sep = '\n')
	return spiral


assert create_spiral(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]