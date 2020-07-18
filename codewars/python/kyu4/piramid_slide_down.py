# https://www.codewars.com/kata/551f23362ff852e2ab000037

class Node:
	def __init__(self, value):
		self.value = value
		self.path_value = None
		self.left = None
		self.top_left = None
		self.right = None
		self.top_right = None

	def __str__(self):
		return str(self.value)


def get_nodes(pyramid):
	nodes = []
	for i in pyramid:
		row = []
		for j in i:
			row.append(Node(j))
		nodes.append(row)

	for row in range(len(nodes)-1):
		for col in range(len(nodes[row])):
			nodes[row][col].left = nodes[row + 1][col]
			nodes[row + 1][col].top_right = nodes[row][col]
			nodes[row][col].right = nodes[row + 1][col + 1]
			nodes[row + 1][col + 1].top_left = nodes[row][col]

	return nodes


def fill_path_value(node):

	if node.path_value is None:
		max_ = 0
		if node.top_left and node.top_left.path_value:
			max_ = node.top_left.path_value
		if node.top_right and node.top_right.path_value:
			max_ = max(max_, node.top_right.path_value)

		node.path_value = node.value + max_

	if node.left is not None:
		fill_path_value(node.left)
	if node.right is not None:
		fill_path_value(node.right)


def longest_slide_down(pyramid):

	nodes = get_nodes(pyramid)
	start = nodes[0][0]

	fill_path_value(start)

	for row in nodes:
		print(f"{' '.join(str(i.path_value) for i in row)}")

	print(max([i.path_value for i in nodes[-1]]))
	return max([i.path_value for i in nodes[-1]])


assert longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 23

assert longest_slide_down([
			[75],
			[95, 64],
			[17, 47, 82],
			[18, 35, 87, 10],
			[20,  4, 82, 47, 65],
			[19,  1, 23, 75,  3, 34],
			[88,  2, 77, 73,  7, 63, 67],
			[99, 65,  4, 28,  6, 16, 70, 92],
			[41, 41, 26, 56, 83, 40, 80, 70, 33],
			[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
			[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
			[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
			[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
			[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
			[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]) == 1074
