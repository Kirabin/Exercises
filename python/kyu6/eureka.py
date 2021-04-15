# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python


def is_eureka(num):

	s = 0
	for i, c in enumerate(str(num), 1):
		s += int(c)**i

	return s == num


def sum_dig_pow(a, b):

	res = []
	for i in range(a, b + 1):

		if is_eureka(i):
			res.append(i)

	return res


assert sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
assert sum_dig_pow(10, 89) ==  [89]
assert sum_dig_pow(10, 100) ==  [89]
assert sum_dig_pow(90, 100) == []
assert sum_dig_pow(89, 135) == [89, 135]