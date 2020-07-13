# Somehow 6 tests AAAAAAAAAAaaaaaa.

def rev_char(c, n): 
	if 'a' <= c <= 'z' : 
		return chr( (ord(c)-ord('a')+n) % 26 + ord('a'))
	elif 'A' <= c <= 'Z':
		return chr( (ord(c)-ord('A')+n) % 26 + ord('A'))
	else:
		return c

def split_string(s): 

	word = ''
	words = []
	for i in range(len(s)): 
		if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z': 
			word += s[i]
		else: 
			if word: words.append(word)
			words.append(s[i])
			word = ''
	if word: words.append(word)
	return words


inp = input() 

words = split_string(inp)
# print(words)
for i in words: 	
	for j in i: 
		print(rev_char(j, len(i)), end='')
print()
	