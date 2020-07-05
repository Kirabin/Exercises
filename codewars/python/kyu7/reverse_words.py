# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(text):
	rev = iter("".join([i[::-1] for i in text.split()]))
	
	res = ""
	for i in text: 
		res += next(rev) if i != " " else i

	return res

# Other's solution
# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))  # .split() != .split(' ')


assert reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'
assert reverse_words('apple') == 'elppa'
assert reverse_words('a b  c d') == 'a b  c d'
assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow'
