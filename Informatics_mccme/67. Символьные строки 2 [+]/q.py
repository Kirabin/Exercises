inp = input() 

d_latters = {}

for i in inp: 
	i = i.upper()
	if 'A' <= i<= 'Z': 
		if i in d_latters: 
			d_latters[i] += 1
		else:
			d_latters[i] = 1

l_latters = sorted(d_latters.items(), reverse = True) 
# print(l_latters)

odd_one = ''
poly_str = ''
for k,v in l_latters: 
	while v >= 2:
		poly_str += k
		v -= 2
	if v == 1: 
		if odd_one: 
			print('NO')
			break
		odd_one = k
else: 
	print(poly_str + odd_one + poly_str[::-1]) 
