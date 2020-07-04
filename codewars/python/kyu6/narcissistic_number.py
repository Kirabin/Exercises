# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic(value):
	return sum(i**len(str(value)) for i in list(map(int, str(value)))) == value


assert narcissistic(7) is True
assert narcissistic(371) is True
assert narcissistic(122) is False
assert narcissistic(4887) is False
