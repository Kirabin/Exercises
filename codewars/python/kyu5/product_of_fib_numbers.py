# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def productFib(prod):

	a, b = 0, 1
	while a * b < prod:
		a, b = b, a + b

	return [a, b, a * b == prod]


assert productFib(4895) == [55, 89, True]
assert productFib(5895) == [89, 144, False]
