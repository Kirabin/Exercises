n = 5
a = 1 
b = 1 
for i in range(2, n): 
	a, b = b, a+b

print(b)