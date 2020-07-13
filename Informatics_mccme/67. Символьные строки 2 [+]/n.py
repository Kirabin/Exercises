inp = input()

flag = 1
str_nums = ''
for i in inp: 
	if '0' <= i <= '9': 
		flag = 0 
		str_nums += i 

# print(str_nums)
int_nums = [int(i) for i in str_nums] 
int_nums.sort(reverse=True)

print(''.join([str(i) for i in int_nums]))


if flag: print(-1)