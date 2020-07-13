a = input()
new_extension = input()
if '.' not in a: 
	print(a + '.' + new_extension)
else: 
	extension = ''
	name = ''
	flag = 1 
	for i in a[::-1]:
		if i == '.' and flag: 
			flag = 0
		if not flag: 
			name += i 

	name = name[::-1]
	print(name + new_extension)