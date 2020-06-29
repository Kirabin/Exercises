# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python

def find_missing(seq):
	
	step = min(seq[1]-seq[0], seq[2]-seq[1])

	for first, second in zip(seq[:-1], seq[1:]):
		if second - first != step:
			return first + step



assert find_missing([1, 2, 3, 4, 6, 7, 8, 9]) == 5
assert find_missing([1, 5, 7]) == 3
assert find_missing([1, 3, 4, 5, 6, 7, 8, 9]) == 2

