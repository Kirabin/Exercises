# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

def print_res(func):
	def wrapper(*args, **kwargs):
		res = func(*args, **kwargs)
		print(res)
		return res

	return wrapper

@print_res
def sqInRect(lng, wdth):

	if lng == wdth:
		return None

	res = []
	while lng > 0 and wdth > 0:
		lng, wdth = max(lng, wdth) - min(lng, wdth), min(lng, wdth)
		res.append(wdth)

	return res




assert sqInRect(5, 5) is None
assert sqInRect(5, 3) == [3, 2, 1, 1]
