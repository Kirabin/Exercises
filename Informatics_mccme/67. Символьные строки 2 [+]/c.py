def is_cond(s):
	if s.find('R') == s.rfind('B') + 1: 
		return 1
	return 0

inp = input()

count = 0
s = inp 

while not is_cond(s) and len(s) > 0: 
	first_r = s.find('R') 
	last_b = s.rfind('B')
	s = s[:first_r] + s[first_r+1:last_b] + s[last_b+1:]
	count += 2
 
print(s)
print(count)