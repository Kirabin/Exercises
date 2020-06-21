import base64
import codecs


# codecs lib - OK
#
#
my_hex = "72bca9" or "68656c6c6faa"

my_asciib = codecs.decode(my_hex, 'hex')
my_64b = codecs.encode(my_asciib, 'base64')
my_64 = my_64b.decode('ascii')
print(my_asciib)
print(type(my_asciib))
print(my_64b)
print(my_64)




# base64 - KO
#
#
def int_to_ascii(arr):
	s = ''

	for i in arr:
		s += chr(i)

	return s

def hex_to_int(s):

	arr = []
	i = 0
	while i < len(s):
		arr.append(int(s[i: i+2], 16))
		i += 2

	return arr


inp_asciib = int_to_ascii(hex_to_int(my_hex)).encode('utf-8')
inp_64b = base64.b64encode(inp_asciib)
inp_64 = inp_64b.decode()
print(inp_asciib)
print(type(inp_asciib))
print(inp_64b)
print(inp_64)