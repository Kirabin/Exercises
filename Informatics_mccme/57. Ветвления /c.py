a, b, v = 13, 12, 12 or map(int, input().split()) 
if a >= b and a >= v: 
	print('A', end=' ')
if b >= v and b >= a: 
	print('B', end=' ')
if v >= a and v >= b: 
	print('C', end=' ')