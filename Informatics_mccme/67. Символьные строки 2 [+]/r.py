# OK but stupid task (with mistakes)

inp = input()

d = {str(i):0 for i in range(10)}

for i in inp: 
	if '0' <= i <= '9': 
		d[i] += 1

min_num = ''
for k,v in d.items(): 
	if v == 0 and k != '0': 
		min_num += k

if not min_num:
	print(0)
else: 
	print(min_num)