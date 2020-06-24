# https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python

def isPP(n):

	for base in range(2,int(n**0.5) + 1):

		if n % base == 0: 
			power = 0
			n_copy = n
			while n_copy % base == 0:
				power += 1
				n_copy //= base

			if n_copy == 1:
				return [base, power]

	return None



assert isPP(36) == [6,2]
assert isPP(4) == [2,2]
assert isPP(9) == [3,2]
assert isPP(5) == None
