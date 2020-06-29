# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python

def valid_solution(board):

	for i in range(9):
		if (set(board[i]) != set(range(1,10)) or
			set([i for i in zip(*board)]) != set(range(1,10))):
			return False 

	for cube_i in range(0, 7, 3):
		for cube_j in range(0, 7, 3):

			box_values = []
			for i in range(3):
				for j in range(3):
					box_values.append(board[i + cube_i][j + cube_j])

			if set(box_values) != set(range(1,10)):
				return False

	return True




assert valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
					   [6, 7, 2, 1, 9, 5, 3, 4, 8],
					   [1, 9, 8, 3, 4, 2, 5, 6, 7],
					   [8, 5, 9, 7, 6, 1, 4, 2, 3],
					   [4, 2, 6, 8, 5, 3, 7, 9, 1],
					   [7, 1, 3, 9, 2, 4, 8, 5, 6],
					   [9, 6, 1, 5, 3, 7, 2, 8, 4],
					   [2, 8, 7, 4, 1, 9, 6, 3, 5],
					   [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True

assert valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
					   [6, 7, 2, 1, 9, 0, 3, 4, 9],
					   [1, 0, 0, 3, 4, 2, 5, 6, 0],
					   [8, 5, 9, 7, 6, 1, 0, 2, 0],
					   [4, 2, 6, 8, 5, 3, 7, 9, 1],
					   [7, 1, 3, 9, 2, 4, 8, 5, 6],
					   [9, 0, 1, 5, 3, 7, 2, 1, 4],
					   [2, 8, 7, 4, 1, 9, 6, 3, 5],
					   [3, 0, 0, 4, 8, 1, 1, 7, 9]]) == False