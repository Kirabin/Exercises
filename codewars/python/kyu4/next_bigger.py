# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
# Author made mistake in tests

def swaped(s, i, j):
	l = list(s)

	l[i], l[j] = l[j], l[i]
	return ''.join(l)

def next_bigger(n):

	str_n = str(n)
	i = len(str_n) - 1
	while i > 0:
		if int(str_n[i]) > int(str_n[i-1]):
			return int(swaped(str_n, i, i-1))
		if int(str_n[-1]) == 0 and int(str_n[i]) == 0:
			str_n = swaped(str_n, i, i-1)
		i -= 1

	return -1


assert next_bigger(12) == 21
assert next_bigger(513) == 531
assert next_bigger(2017) == 2071
assert next_bigger(414) == 441
assert next_bigger(144) == 414
assert next_bigger(9) == -1
assert next_bigger(19111) == 91111
assert next_bigger(1234567980) == 1234569708
