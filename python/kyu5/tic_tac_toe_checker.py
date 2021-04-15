# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python

def is_solved(board):
	'''
	Return:
		-1: game unfinished
		0 : draw
		1 : x won
		2 : o won
	'''

	# horizontal
	for row in range(3):
		if set(board[row]) in [{2}, {1}]:
			return set(board[row]).pop()

	# vertical
	for col in range(3):
		if set(i[col] for i in board) in [{2}, {1}]:
			return set(i[col] for i in board).pop()


	# diagonal
	if set([board[0][0], board[1][1], board[2][2]]) in [{2}, {1}]:
		return set([board[0][0], board[1][1], board[2][2]]).pop()

	if set([board[0][2], board[1][1], board[2][0]]) in [{2}, {1}]:
		return set([board[0][0], board[1][1], board[2][2]]).pop()

	# count zeroes
	if [board[i][j] for i in range(3) for j in range(3)].count(0) == 0:
		return 0

	return -1


# not yet finished
board = [[0, 0, 1],
		 [0, 1, 2],
		 [2, 1, 0]]
assert is_solved(board) == -1

# winning row
board = [[1, 1, 1],
		 [0, 2, 2],
		 [0, 0, 0]]
assert is_solved(board) == 1

# winning column
board = [[2, 1, 2],
		 [2, 1, 1],
		 [1, 1, 2]]
assert is_solved(board) == 1

# draw
board = [[2, 1, 2],
		 [2, 1, 1],
		 [1, 2, 1]]
assert is_solved(board) == 0