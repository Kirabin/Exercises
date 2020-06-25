# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def validBraces(string):

	queue = []
	braces = {"]": "[", ")": "(", "}": "{"}
	for i in string: 

		if i in braces.values():
			queue.append(i)

		elif i in braces.keys():
			if not queue or queue.pop() != braces[i]:
				return False


	if not queue:
		return True
	return False

assert validBraces("()") == True
assert validBraces("[(])") == False
assert validBraces("(([") == False
assert validBraces(")(}{][)") == False