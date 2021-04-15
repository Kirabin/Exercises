# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

def adjacent_is_one(i, j, spiral):

	adj_i = ((-1, 0),(0, 1),(1, 0),(0, -1))
	adj_count = 0
	for x, y in adj_i:
		try: 
			if i + x >= 0 and j + y >= 0 and spiral[i + x][j + y] == 1:
				adj_count += 1
		except IndexError: 
			pass

	return adj_count > 1


def spiralize(size):

	spiral = [[0 for j in range(size)] for i in range(size)]
	offset = 0
	i, j = 0, -1

	while offset <= size // 2:
		while j < size - offset - 1:
			j += 1
			spiral[i][j] = 1

		while i < size - offset - 1:
			i += 1
			spiral[i][j] = 1

		while j > 0 + offset:
			j -= 1
			spiral[i][j] = 1

		offset += 2
		while i > 0 + offset:
			i -= 1
			spiral[i][j] = 1
		
	if spiral[i][j] == 1 and adjacent_is_one(i, j, spiral):
		spiral[i][j] = 0

	return spiral


assert spiralize(1) == [[1]]

assert spiralize(2) == [[1, 1],
						[0, 1]]

assert spiralize(5) == [[1,1,1,1,1],
						[0,0,0,0,1],
						[1,1,1,0,1],
						[1,0,0,0,1],
						[1,1,1,1,1]]
						
assert spiralize(8) == [[1,1,1,1,1,1,1,1],
						[0,0,0,0,0,0,0,1],
						[1,1,1,1,1,1,0,1],
						[1,0,0,0,0,1,0,1],
						[1,0,1,0,0,1,0,1],
						[1,0,1,1,1,1,0,1],
						[1,0,0,0,0,0,0,1],
						[1,1,1,1,1,1,1,1]]