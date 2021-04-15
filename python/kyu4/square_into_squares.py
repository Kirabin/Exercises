# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

def decompose(n):
	res = [n]
	goal = 0
	while res:
		current = res.pop()
		goal += current ** 2

		for j in range(current - 1, 0, -1):
			if goal - j ** 2 >= 0:
				goal -= j ** 2
				res.append(j)

				if goal == 0:
					return sorted(res)


assert decompose(2) is None
assert decompose(11) == [1, 2, 4, 10]
assert decompose(5) == [3, 4]
assert decompose(8) is None
assert decompose(50) == [1, 3, 5, 8, 49]
