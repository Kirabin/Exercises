# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

# Best 
# def scramble(s1, s2):
# 	for i in set(s2):
# 		if s1.count(i) < s2.count(i):
# 			return False
# 	return True


# My 
def scramble(s1, s2):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	d1 = {}
	d2 = {}

	for i in alphabet:  
		d1[i] = s1.count(i)

	for i in alphabet:  
		d2[i] = s2.count(i)

	
	for ch, vl in d2.items(): 
		if vl > d1.get(ch, 0):
			return False

	return True


assert scramble('rkqodlw', 'world') == True
assert scramble('cedewaraaossoqqyt', 'codewars') == True
assert scramble('katas', 'steak') == False
assert scramble('scriptjava', 'javascript') == True
assert scramble('scriptingjava', 'javascript') == True