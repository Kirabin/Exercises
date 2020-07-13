def character(code): 
	if 0 < code < 9: 
		return str(code)
	return chr(code - 10 + ord('A'))

def to_system(num, sys):
	converted_num = ''
	minus_flag = 0
	if num < 0: 
		num *= -1
		minus_flag = 1
	while num: 
		converted_num = character(num%sys) + converted_num
		num //= sys

	return '-'*minus_flag + converted_num

def to_dec(num_str, sys): 
	pass

dec_num, system = 25, 3
print(to_system(dec_num, system))