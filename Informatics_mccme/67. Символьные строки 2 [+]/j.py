inp = input()

numbers = list(map(int, inp.replace('-', '+').split('+')))
opers = [i for i in inp if i in '+-']

s = numbers[0]
for num, oper in zip(numbers[1:], opers): 
	
	if oper == '-': 
		s -= num
	elif oper == '+':
		s += num

print(s) 