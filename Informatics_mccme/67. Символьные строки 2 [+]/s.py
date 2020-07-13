# Fed up with it, doesn't support ax^2+c = 0 
# Not worth it

from math import sqrt
def solve_equation(s): 
	a = float(s[:s.find('a')] or 1)

	s1 = s[s.find('a')+1:s.find('b')]
	b = float(s1 if len(s1) > 1 else 1)
	c = float(s[s.find('b')+1:])
	# print(a, b, c)
	d = b*b - 4*a*c
	# print(d)
	if d == 0: 
		x1 = -b / 2*a
		return [x1]
	elif d < 0: 
		return []
	else: 		
		# print(-b + d**0.5)
		x1 = (-b + sqrt(d)) / (2*a)
		x2 = (-b - sqrt(d)) / (2*a)
		return [x1, x2]

inp = input()

x = solve_equation(inp)
for i in sorted(x): 
	# print(i)
	print('%.3f' % i, end=' ')