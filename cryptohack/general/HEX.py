def ascii(arr):
	s = ''

	try:
		iter(arr)
	except TypeError:
		arr = [arr]

	for i in arr:
		s += chr(i)

	return s

def hex_to_ascii(s):

	arr = []
	i = 0
	while i < len(s):
		arr.append(int(s[i: i+2], 16))
		i += 2

	return arr



inp = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print(ascii(hex_to_ascii(inp)))


print(ascii(45))