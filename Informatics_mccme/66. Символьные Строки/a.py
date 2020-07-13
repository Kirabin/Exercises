a = input()

count = 0
new_str = ''
for i in a: 
	if i == 'a':
		new_str += 'b'
		count += 1
	else: new_str += i

print(new_str)
print(count)