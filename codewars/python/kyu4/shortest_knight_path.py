# https://www.codewars.com/kata/549ee8b47111a81214000941/train/python

def available(point, field):
	new_points = []

	i, j = point

	for relative_i, relative_j in [(1, 2), (-1, 2), (2, -1), (-2, -1), (-1, -2), (1, -2), (-2, 1), (2, 1)]:
		if (0 <= i + relative_i < 8 and 
			0 <= j + relative_j < 8 and
			field[i + relative_i][j + relative_j] == 100):

			new_points.append((i + relative_i, j + relative_j))

	return new_points


def fill_field(point, field, steps):

	field[point[0]][point[1]] = min(field[point[0]][point[1]], steps)

	points = [point]
	while points: 
		for point in points[:]:

			del points[0]
			new_points = available(point, field)
			for new_point in new_points:

				if field[new_point[0]][new_point[1]] == 100:
					field[new_point[0]][new_point[1]] = steps


			points.extend(new_points)

		steps += 1


def knight(p1, p2):
	# field[i][j] 
	# i - rows (numbers)
	# j - cols (letters)

	start = (int(p1[1])-1, ord(p1[0]) - ord('a'))
	dest = (int(p2[1])-1, ord(p2[0]) - ord('a'))

	field = [[100 for _ in range(8)] for _ in range(8)]
	field[start[0]][start[1]] = 0

	fill_field(start, field, 1)
	
	return field[dest[0]][dest[1]]



arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]

for i in arr: 
	assert knight(i[0], i[1]) == i[2]


