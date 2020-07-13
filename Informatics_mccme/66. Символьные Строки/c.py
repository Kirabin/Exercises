a = input()

count = 0
new_str = ''
for i in a: 
	if i in 'aAbB':
		new_str += 'aAbB'[('aAbB'.find(i)+2)%4]
		count += 1
	else: 
		new_str += i

print(new_str)
print(count)