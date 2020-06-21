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