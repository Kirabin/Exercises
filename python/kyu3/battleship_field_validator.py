# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

def check_diagonals(i, j, field): 

	for x, y in zip([-1, -1, 1, 1], [-1, 1, 1, -1]):
		if (0 <= i + x < 10 and 0 <= j + y < 10 and field[i+x][j+y] == 1):
			print(f"diagonal at ({i}, {j}) - ({i + x}, {j + y})")
			return False

	return True


def fill_ship(i, j, field):

	field[i][j] = 1
	size = 1

	# vertical
	while (0 <= i + size < 10 and field[i+size][j] is None):
		field[i+size][j] = 1
		size += 1

	if size != 1:
		return size

	# horizontal
	while (0 <= j + size < 10 and field[i][j+size] is None):
		field[i][j+size] = 1
		size += 1

	return size


def validate_battlefield(field):

	valid_ships_count = {1: 4, 2: 3, 3: 2, 4: 1}
	ships 			  = {1: 0, 2: 0, 3: 0, 4: 0}
	been_there_field = [[None if j else 0 for j in i] for i in field ]

	
	# check for diagonals
	for i in range(10): 
		for j in range(10): 
			if field[i][j] == 1 and check_diagonals(i, j, field) is False:
				return False 

	# check for ships amount
	for i in range(10): 
		for j in range(10): 
			if been_there_field[i][j] is None:
				try:
					ships[fill_ship(i, j, been_there_field)] += 1
				except KeyError:
					print("no ships this size allowed")
					return False


	if ships == valid_ships_count:
		return True
	else:
		print(f"Ships: {ships} AmountError")
		return False




assert validate_battlefield(
[[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) is True


assert validate_battlefield(
[[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
 [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) is False


assert validate_battlefield(
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
 [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]) is True