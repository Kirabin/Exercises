# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(strings, markers):

	res = []
	for string in strings.split("\n"):

		new_str = ""
		for char in string: 
			if char in markers:
				break
			new_str += char

		res.append(new_str.rstrip())

	return "\n".join(res)



assert solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples, pears\ngrapes\nbananas"
assert solution("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd"