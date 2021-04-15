# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

def tickets(people):

	lowest = 0
	middle = 0 
	for i in people:
		if i == 25:
			lowest += 1
		elif i == 50: 
			if lowest >= 1:
				lowest -= 1
				middle += 1
			else:
				return "NO"
		elif i == 100: 
			if lowest >= 1 and middle >= 1: 
				lowest -= 1
				middle -= 1
			elif lowest >= 3:
				lowest -= 3
			else: 
				return "NO"

	return "YES"


assert tickets([25, 25, 50]) == "YES"
assert tickets([25, 100]) == "NO"
assert tickets([25, 25, 50, 50, 100]) == "NO"

