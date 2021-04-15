# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(numbers, target):

	prev = {}
	for i, x in enumerate(numbers):

		if target - x in prev:
			return [prev[target - x], i]

		prev[x] = i


assert sorted(two_sum([1, 2, 3], 4)) == [0, 2]
assert sorted(two_sum([1234, 5678, 9012], 14690)) == [1, 2]
assert sorted(two_sum([2, 2, 3], 4)) == [0, 1]
