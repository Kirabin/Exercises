# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

def zeros(n):

	count = 0

	k = 5
	while k <= n: 
		count += n // k
		k *= 5

	return count



assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7 
assert zeros(1000) == 249