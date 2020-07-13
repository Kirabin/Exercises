def is_simple(a): 
	if a%2 == 0: 
		return 0 
	
	i = 3
	while i*i < a: 
		if a%i == 0: return 0
		i += 2
	return 1

inp = 733

for i in range(len(str(inp))): 
	if not is_simple(inp//10**i):
		print("NO")
		break
else: 
	print("YES")