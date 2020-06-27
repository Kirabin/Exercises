# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):

	d = {}
	for i in word: 
		d[i.lower()] = d.get(i.lower(), 0) + 1

	res = ""
	for i in word: 
		if d.get(i.lower(), 0) >= 2: 
			res += ")"
		else:
			res += "("

	return res



assert duplicate_encode("din") == "((("
assert duplicate_encode("recede") == "()()()"
assert duplicate_encode("Success") == ")())())"
assert duplicate_encode("(( @") == "))(("
assert duplicate_encode("Qz!dHQzPIxvca u@OHcwJaS@H) QIxk@bb") == "))(()))())()))()())(()())())))()))"