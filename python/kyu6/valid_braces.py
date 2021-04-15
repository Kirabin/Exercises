# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def validBraces(string):

	stack = []
	braces = {"]": "[", ")": "(", "}": "{"}
	for i in string: 

		if i in braces.values():
			stack.append(i)

		elif i in braces.keys():
			if not stack or stack.pop() != braces[i]:
				return False

	return len(stack) == 0


assert validBraces("()") == True
assert validBraces("[(])") == False
assert validBraces("(([") == False
assert validBraces(")(}{][)") == False