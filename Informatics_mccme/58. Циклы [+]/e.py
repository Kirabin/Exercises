start, end = 2, 5 or map(int, input().split()) 

s = 0
for i in range(start, end+1):
	s += i*i 
print(s)