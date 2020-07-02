# https://www.codewars.com/kata/5296bc77afba8baa690002d7

def cell_possibilities(puzzle, i, j):
	# get possible values that can be put on puzzle[i][j]

	possible = set(range(1,10))
	occupied = set()
	occupied.update(puzzle[i]) # horizontal
	occupied.update(list(zip(*puzzle))[j]) # vertical

	cube_i = i // 3 * 3
	cube_j = j // 3 * 3
	for i in range(3):
		for j in range(3):
			occupied.add(puzzle[i + cube_i][j + cube_j]) # cube

	return possible - occupied


def sudoku(puzzle, i = 0, j = 0):
	if i > 8:
		return puzzle

	if puzzle[i][j] != 0:
		sol = sudoku(puzzle, i + (j + 1) // 9, (j + 1) % 9)
		if sol:
			return sol

	else:
		possib = cell_possibilities(puzzle, i, j)
		if not possib:
			return None

		sol = None
		for variant in possib:
			puzzle[i][j] = variant
			sol = sudoku(puzzle, i + (j + 1) // 9, (j + 1) % 9)
			if sol:
				return sol
				break 
		puzzle[i][j] = 0 
		return None if not sol else sol


puzzle = [[5,3,0,0,7,0,0,0,0],
		  [6,0,0,1,9,5,0,0,0],
		  [0,9,8,0,0,0,0,6,0],
		  [8,0,0,0,6,0,0,0,3],
		  [4,0,0,8,0,3,0,0,1],
		  [7,0,0,0,2,0,0,0,6],
		  [0,6,0,0,0,0,2,8,0],
		  [0,0,0,4,1,9,0,0,5],
		  [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
			[6,7,2,1,9,5,3,4,8],
			[1,9,8,3,4,2,5,6,7],
			[8,5,9,7,6,1,4,2,3],
			[4,2,6,8,5,3,7,9,1],
			[7,1,3,9,2,4,8,5,6],
			[9,6,1,5,3,7,2,8,4],
			[2,8,7,4,1,9,6,3,5],
			[3,4,5,2,8,6,1,7,9]]

assert sudoku(puzzle) == solution