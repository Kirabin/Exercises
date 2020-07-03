# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(floors):

	res = []
	for asterisks in range(1, floors*2, 2):
		res.append(f"{'*'*asterisks:^{floors*2-1}}")

	return res

assert tower_builder(1) == ['*', ]
assert tower_builder(2) == [' * ', '***']
assert tower_builder(3) == ['  *  ', ' *** ', '*****']