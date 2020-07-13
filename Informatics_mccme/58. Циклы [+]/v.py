s = 0
inp = int(input())
min_num = 10000
max_num = 0
while inp: 
	if inp < min_num:
		min_num = inp 
	if inp > max_num:
		max_num = inp
		
	inp = int(input())
print(min_num, max_num)
