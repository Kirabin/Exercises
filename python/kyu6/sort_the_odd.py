# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):

	odd = sorted([i for i in source_array if i % 2 == 1])

	res = []
	for i in source_array:
		if i % 2 == 1:
			res.append(odd.pop(0))
		else:
			res.append(i)

	return res


assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
assert sort_array([]) == []