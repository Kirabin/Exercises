inp = input()


flag = 0 
count = 0
for i in inp[::-1]: 
	if i == 'R': 
		flag = 1 
	if flag and i =='B':
		count += 1
		continue 
	print(i, end='')
print()
print(count)