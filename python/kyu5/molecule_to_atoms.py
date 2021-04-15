# https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python

def formula_to_list(formula):
	# Format string of molecules and operators to list
	# 0. "K4[ON(SO3)2]2"
	# 1. [{'K': 1}, '*', '4', '+', '(', {'O': 1}, '+', {'N': 1}, '+', '(', {'S': 1}, '+', {'O': 1}, '*', '3', ')', '*', '2', ')', '*', '2']


	formula_l = []
	i = 0
	while i < len(formula):
		if formula[i].isalpha():
			if i + 1 < len(formula) and formula[i + 1].islower():
				if formula_l and formula_l[-1] != "(":
					formula_l.append("+")
				formula_l.append({formula[i:i+2]: 1})
				i += 1
			else: 
				if formula_l and formula_l[-1] != "(":
					formula_l.append("+")
				formula_l.append({formula[i]: 1})

		elif formula[i].isdigit():	
			j = 0
			while i + j + 1 < len(formula) and formula[i + j+ 1].isdigit():
				j += 1

			if formula_l: 
				formula_l.append('*')
			formula_l.append(formula[i:i+j+1])
			i += j
		else:
			if formula_l and formula[i] == "(":
				formula_l.append("+")
			formula_l.append(formula[i])
		i += 1

	return formula_l


def list_to_rp_notion(formula):
	# to Reverse Polish Notation
	# 0. [{'K': 1}, '*', '4', '+', '(', {'O': 1}, '+', {'N': 1}, '+', '(', {'S': 1}, '+', {'O': 1}, '*', '3', ')', '*', '2', ')', '*', '2']
	# 1. [{'K': 1}, '4', '*', {'O': 1}, {'N': 1}, '+', {'S': 1}, {'O': 1}, '3', '*', '+', '2', '*', '+', '2', '*', '+']

	rp_notation = []
	oper_stack = []

	for i in formula: 

		if type(i) == dict or i.isdigit():
			rp_notation.append(i)

		elif i in "+*":
			while (oper_stack 
				   and oper_stack[-1] != "("
				   and "+*".index(oper_stack[-1]) >= "+*".index(i)):
				rp_notation.append(oper_stack.pop())
			oper_stack.append(i)
		elif i in "(":
			oper_stack.append(i)
		elif i in ")":
			while (oper_stack
				   and oper_stack[-1] != "("):
				rp_notation.append(oper_stack.pop())
			if oper_stack[-1] == "(":
				oper_stack.pop()

	while oper_stack:
		rp_notation.append(oper_stack.pop())

	return rp_notation


def solve_rp_notation(rp_notation):
	
	stack = []
	for i in rp_notation: 

		# print (stack, i)
		if type(i) == dict or i.isdigit():
			stack.append(i)

		if i == "*":
			factor = int(stack.pop())
			molecules = stack.pop() 
			for molecule, amount in molecules.items():
				molecules[molecule] = amount * factor 

			stack.append(molecules)

		if i == "+": 
			mole_2 = stack.pop() if stack else {}
			mole_1 = stack.pop() if stack else {}
			new_mole = {}
			for mole, amount in list(mole_1.items()) + list(mole_2.items()):
				new_mole[mole] = new_mole.get(mole, 0) + amount

			stack.append(new_mole)

		# print(stack, end="\n\n")

	return stack[0]


def parse_molecule (formula):
	formula = formula.replace("[", "(").replace("]",")").replace("{", "(").replace("}", ")")
	formula = formula_to_list(formula)

	# print(formula, end ='\n\n')
	rp_notation = list_to_rp_notion(formula)
	# print(rp_notation, end ='\n\n')
	res = solve_rp_notation(rp_notation)
	# print(res)

	return res


parse_molecule("As2{Be4C5[BCo3(CO2)3]2}4Cu5")
assert parse_molecule("H(H2)2") == {'H': 5} # [{'H': 1}, '+', '(', {'H': 1}, "*", "2", ')', '*', '2']

# [{'H': 1}, '+', '(', {'H': 1}, "*", "2", ')', '*', '3']
# [{'H': 1}, '+', {'H': 1}, "2", "*", "3", '*']
# [{'H': 7}]
assert parse_molecule("H(H2)3") == {'H': 7}

assert parse_molecule("(H(H2)2)2") == {'H': 10}
assert parse_molecule("H2O") == {'H': 2, 'O' : 1}
assert parse_molecule("(H2O)2") == {'H': 4, 'O' : 2}
assert parse_molecule("Mg11(OH)12") == {'Mg': 11, 'O' : 12, 'H': 12}
assert parse_molecule("K4[ON(SO3)2]2") == {'K': 4,  'O': 14,  'N': 2,  'S': 4}