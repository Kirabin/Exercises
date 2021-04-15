# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python

def who_is_next(names, r):
	
	names = [{i: 1} for i in names]

	while 1:
		[(name, count)] = names.pop(0).items()

		r -= count
		if r <= 0:
			return name

		names.append({name: count*2})




names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

assert who_is_next(names, 1) == "Sheldon"
assert who_is_next(names, 52) == "Penny"
assert who_is_next(names, 7230702951) == "Leonard"