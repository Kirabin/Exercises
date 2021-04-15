# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def num_sum(n): 
	s = 0

	while n != 0: 
		s += n % 10
		n //= 10

	return s

def digital_root(n):

	temp = n
	while n // 10 != 0: 
		
		n = num_sum(n)

	return n



assert digital_root(16) == 7
assert digital_root(942) == 6
assert digital_root(132189) == 6
assert digital_root(493193) == 2