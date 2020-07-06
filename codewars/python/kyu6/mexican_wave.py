# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

def wave(people):

	res = []
	for i, c in enumerate(people):
		if c == " ":
			continue
		res.append(people[:i] + c.upper() + people[i+1:])

	return res



result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
assert wave("hello") == result

result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
assert wave("codewars") == result

result = []
assert wave("") == result

result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
assert wave("two words") == result

result = [" Gap ", " gAp ", " gaP "]
assert wave(" gap ") == result