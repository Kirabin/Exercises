# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python

from itertools import combinations


def choose_best_sum(limit_distance, limit_towns, distances):

	pairs = []
	max_distance = 0
	distances.sort()

	for i in combinations(distances, limit_towns):
		trip = sum(i)

		if max_distance < trip <= limit_distance:
			max_distance = trip 

	return max_distance or None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
assert choose_best_sum(230, 4, xs) == 230
assert choose_best_sum(430, 5, xs) == 430
assert choose_best_sum(430, 8, xs) == None