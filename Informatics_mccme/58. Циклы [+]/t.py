n = int(input()) 
s = 0
p = 1
for i in range(n): 
	a = int(input())
	s += a
	p *= a

print(s,  p)