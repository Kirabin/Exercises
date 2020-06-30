# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
# I know, I know it's bad, I realized afterwards


def find_nb(m):
	
	s = 0
	n = 1
	while s < m:		
		s = (n * (n + 1) // 2) ** 2 # sum of 1..n powered by 3	
		n += 1

	if s == m: 

		return n-1

	return -1

find_nb(1034345037459002500)
assert find_nb(1071225) == 45
assert find_nb(4183059834009) == 2022
assert find_nb(24723578342962) == -1
assert find_nb(135440716410000) == 4824
assert find_nb(40539911473216) == 3568
assert find_nb(26825883955641) == 3218