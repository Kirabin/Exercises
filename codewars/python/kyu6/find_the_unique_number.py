# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

from collections import Counter

def find_uniq(arr):
	return Counter(arr).most_common()[-1][0]



assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10