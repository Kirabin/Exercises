import re 

def solve(s): 
	nums = list(map(int, re.split('[/*]', s)))
	opers = [i for i in s if i in '*/']

	res = nums[0]
	for n, o in zip(nums[1:], opers): 
		if o == '*': 
			res *= n
		else: 
			res //= n
	return res 


inp = input()

nums = re.split('[+-]', inp)
opers = [i for i in inp if i in '+-']

s = solve(nums[0])

for n, o in zip(nums[1:], opers): 
	if o == '-': 
		s -= solve(n)
	else: 
		s += solve(n)

print(s)