# https://www.codewars.com/kata/5904be220881cb68be00007d/train/python

def fish(shoal):

	amount_needed = 4
	fish_size = 1
	eaten = 0
	for i in sorted(shoal, key = lambda x: int(x)):
		if int(i) <= fish_size: 
			eaten += int(i)

			if eaten >= amount_needed:
				fish_size += 1
				eaten -= amount_needed
				amount_needed += 4
				
	return fish_size




assert fish("") == 1
assert fish("0") == 1
assert fish("6") == 1
assert fish("1111") == 2
assert fish("11112222") == 3
assert fish("111122223333") == 4
assert fish("111111111111") == 3
assert fish("111111111111111111112222222222") == 5
assert fish("151128241212192113722321331") == 5