# Калькулятор - выражения со скобками 
# Somehow it passed only 9 tests

def split_string(s): 
	i = 0
	l = [] 
	num = ''
	while i < len(s): 
		if s[i] in '()+*/': 
			if num: 
				l.append(num) 
				num = ''
			l.append(s[i])
		elif s[i] == '-' and i-1 >= 0 and (s[i-1] in '0123456789)'): 
			if num: 
				l.append(num) 
				num = ''
			l.append(s[i])
		elif s[i] == '-' and s[i+1] in '(': 
			l.append('0')
			l.append('-')
		else: 	
			num += s[i]
		i+= 1

	if num: l.append(num)
	return l

def prior(c): 
	if c in '()': 
		return 0
	if c in '+-': 
		return 1
	if c in '*/':
		return 2

def to_polish_notation(l): 

	stack = []
	res_str = ''
	for i in l: 
		if '0' <= i[-1] <= '9':
			res_str += i + ' '

		elif i in '/*-+':
			if stack and prior(stack[-1]) >= prior(i): 
				res_str += stack.pop() + ' '
				stack.append(i)
			else: 
				stack.append(i)

		elif i == '(': 
			stack.append(i)

		elif i == ')': 
			while stack[-1] != '(': 
				res_str += stack.pop() + ' '
			stack.pop()

	for i in stack[::-1]: 
		res_str += i + ' '

	return res_str

def solve_polish_notation(s): 
	stack = []
	for i in s.split(): 
		if '0' <= i[-1] <= '9':
			stack.append(int(i))
		else: 
			second_n = stack.pop()
			first_n = stack.pop()

			if i == '+': 
				r = first_n + second_n
			elif i == '-': 
				r = first_n - second_n 
			elif i == '/':
				if second_n == 0: 
					return 0 #
				r = first_n // second_n

			elif i == '*': 
				r = first_n * second_n

			stack.append(r)

	return stack.pop()

inp = input()

nums_and_opers = split_string(inp)
# print(nums_and_opers)
polish_notation_string = to_polish_notation(nums_and_opers)
# print(polish_notation_string)
res = solve_polish_notation(polish_notation_string)
print(res) 