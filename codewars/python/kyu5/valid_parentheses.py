# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):	
	queue = []

	for i in string:
		if i in "()":
			if queue and queue[-1] + i == '()':
				queue.pop()
			else:
				queue.append(i)

	return not queue



a = "hi(hi)()"
a = "(())((()())())"

print(valid_parentheses(a))