def to_oct(num): 
	oct_num = oct(num)[2:]
	return '0'*(10-len(oct_num)) + oct_num


inp = 65
print(to_oct(inp))