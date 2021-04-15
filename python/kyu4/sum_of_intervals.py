# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
# It was easier than I thought

def sum_of_intervals(intervals):

	res = set()
	for start, end in intervals: 
		res.update(range(start, end))

	return len(res)



assert sum_of_intervals([(1, 5)]) == 4
assert sum_of_intervals([(1, 5), (6, 10)]) == 8
assert sum_of_intervals([(1, 5), (1, 5)]) == 4
assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7