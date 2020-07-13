a = input().split()

max_len = 0 
max_word = ''
for i in a: 
	if len(i) > max_len: 
		max_len = len(i)
		max_word = i

print(max_word)
print(max_len)