def to_hex(num): 
	hex_num = hex(num)[2:].upper()
	
	# EDIT: just use .upper()
	# f -> F
	# hex_num = ''.join([chr(ord(i)-ord('a') + ord('A')) for i in hex_num])

	return '0'*(4-len(hex_num)) + hex_num


inp = 255
print(to_hex(inp))