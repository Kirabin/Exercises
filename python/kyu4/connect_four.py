# https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python

def print_field(field):

	for i in field:
		for j in i: 
			print(j, end = ' ')
		print()
	print()


def check_win(row, col, color, field):
	
	col = ord(col) - ord('A')
	
	# check horizontal 
	for j in range(0, 4):
		quad = field[row][j:j+4]
		if set(quad) in [{'Y'}, {'R'}]:
			return color

	# check vertical
	for i in range(0, 3):
		quad = [field[i][col] for i in range(i, i + 4)] 
		if set(quad) in [{'Y'}, {'R'}]:
			return color

	# check left-to-right diagonal
	j = max(col - row, 0)
	i = max(row - col, 0)
	diagonal_items = []

	while j < 7 and i < 6:
		diagonal_items.append(field[i][j])
		i += 1
		j += 1

	for j in range(0, len(diagonal_items) - 4 + 1):
		quad = diagonal_items[j: j + 4]
		if set(quad) in [{'Y'}, {'R'}]:
			return color

	# check right-to-left diagonal
	j = min(col + row, 6)
	i = max(row - (6 - col), 0)
	diagonal_items = []

	while j >= 0 and i < 6:
		diagonal_items.append(field[i][j])
		j -= 1
		i += 1

	for j in range(0, len(diagonal_items) - 4 + 1):
		quad = diagonal_items[j: j + 4]
		if set(quad) in [{'Y'}, {'R'}]:
			return color


def put_piece(col, color, field):
	
	i = 0
	j = ord(col) - ord('A')

	while i < 6 and field[i][j] == 0:
		i += 1

	field[i-1][j] = color[0]
	return i-1


def who_is_winner(pieces_position_list):

	field = [[0 for _ in range(7)] for _ in range(6)]

	for col, color in map(lambda x: x.split('_'), pieces_position_list): 
		row = put_piece(col, color, field)
		res = check_win(row, col, color, field)
		if res: 
			return res

	return "Draw"




assert who_is_winner(["B_Red", "C_Red", "D_Red", "E_Red", "F_Red", "G_Red"
	]) == "Red"

assert who_is_winner(["D_Red", "E_Red", "F_Red", "G_Red"
	]) == "Red"

assert who_is_winner(["D_Red", "E_Yellow", "F_Red", "G_Red", "D_Yellow", "E_Yellow", "F_Yellow", "G_Yellow"
	]) == "Yellow"

assert who_is_winner([ 
"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", 
"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]) == "Yellow"

assert who_is_winner([
"C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red", 
"G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red", 
"D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red", 
"C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red", 
"E_Yellow", "E_Red"
]) == "Yellow"
	
assert who_is_winner([
"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", 
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", 
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red", 
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", 
"B_Yellow", "B_Red"
]) == "Red"

assert who_is_winner([
"A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
"G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
]) == "Red"

assert who_is_winner([
"A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"
]) == "Yellow"

assert who_is_winner([ 
"A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"
]) == "Draw"