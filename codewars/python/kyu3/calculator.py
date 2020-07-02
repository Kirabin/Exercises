# https://www.codewars.com/kata/5235c913397cbf2508000048/train/python

class Calculator(object):

	def evaluate(self, string):
		print(f"String:                  {string}")

		nums_and_opers = string.replace(')', ' ) ').replace('(', ' ( ').split()
		print(f"List interpretation:     {nums_and_opers}")

		polish_notation = self.to_polish_notation(nums_and_opers)
		print(f"Reverse Polish Notation: {polish_notation}")

		res = self.solve_polish_notation(polish_notation)
		print(f"Result: {res}", end="\n\n")
		return res


	def prior(self, c): 
		if c in '()': 
			return 0
		if c in '+-': 
			return 1
		if c in '*/':
			return 2


	def to_polish_notation(self, l): 

		stack = []
		res = []
		for i in l: 
			if i in '/*-+':
				while (stack 
					   and self.prior(stack[-1]) >= self.prior(i)
					   and stack[-1] != "("): 
					res.append(stack.pop())
				stack.append(i)


			elif i == '(': 
				stack.append(i)

			elif i == ')': 
				while stack and stack[-1] != '(': 
					res.append(stack.pop())
				if stack[-1] == "(": 
					stack.pop()
			else:
				try:
					res.append(int(i))
				except:
					try: 
						res.append(float(i))
					except:
						print("Type is not numeral")

		while stack:
			res.append(stack.pop())

		return res


	def solve_polish_notation(self, notation): 
		stack = []
		for i in notation: 
			if type(i) in [float, int]:
				stack.append(i)
			elif i in "()/-+*": 
				second_n = stack.pop() if stack else 0 
				first_n = stack.pop() if stack else 0
				r = 0

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


assert Calculator().evaluate("1.1 + 2.2 + 3.3") == 6.6
assert Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8") == 8
assert Calculator().evaluate("(1 + 1)") == 2
assert Calculator().evaluate("2 / 2 + 3 * 4 - 6") == 7