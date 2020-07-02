# https://www.codewars.com/kata/5262119038c0985a5b00029f/solutions/python

def is_prime(num):

	if num <= 1:
		return False 

	for i in range(2, int(num**0.5) + 1):
		if num % i == 0: 
			return False
			
	return True


assert is_prime(0) == False 
assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(73) == True
assert is_prime(75) == False
assert is_prime(-1) == False