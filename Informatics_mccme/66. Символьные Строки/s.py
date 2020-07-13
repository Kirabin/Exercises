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
	return int(num_str, sys)

num_str = '-253'
old_sys, new_sys = 8, 16 

print(to_system(to_dec(num_str, old_sys), new_sys))
