a, b = 121, 136 or map(int, input().split()) 

count = 0
while a and b: 
	a, b = max(a,b) % min(a,b), min(a,b)
	count += 1	
print(a or b, count)