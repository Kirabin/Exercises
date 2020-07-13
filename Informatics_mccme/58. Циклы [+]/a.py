a, b = -6, -7 or map(int, input().split()) 

flag = ((a<0) + (b<0))%2
a = abs(a); b = abs(b)

s = 0
for i in range(b):
	s += a 

print(('-' if flag else '') + str(s))