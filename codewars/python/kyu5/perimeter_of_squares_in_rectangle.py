# https://www.codewars.com/kata/559a28007caad2ac4e000083/python

def fib(n):
	yield 1
	yield 1

	a, b = 1, 1
	for i in range(2, n + 1):
		a, b = b, a + b
		yield b


def perimeter(n):

	sum_ = 0
	for i in fib(n):
		sum_ += i * 4

	return sum_


assert perimeter(5) == 80
assert perimeter(7) == 216
assert perimeter(20) == 114624
assert perimeter(30) == 14098308
assert perimeter(100) == 6002082144827584333104
