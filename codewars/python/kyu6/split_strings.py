# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

from itertools import zip_longest

def solution(s):
	res = [a + b for a, b in zip_longest(s[::2], s[1::2], fillvalue="_")]
	return res


assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']
assert solution("asdfads") == ['as', 'df', 'ad', 's_']