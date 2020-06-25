# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
	lens = [len(i) for i in s.split()]
	return min(lens)



assert find_short("bitcoin take over the world maybe who knows perhaps") == 3
assert find_short("turns out random test cases are easier than writing out basic ones") == 3
assert find_short("lets talk about javascript the best language") == 3
assert find_short("i want to travel the world writing code one day") == 1
assert find_short("Lets all go on holiday somewhere very cold") == 2