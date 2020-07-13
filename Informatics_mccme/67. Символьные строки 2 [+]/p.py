# 22 out of 25

inp = input()

nums = {}
for i in inp: 
	if '0' <= i <= '9':
		if i in nums: 
			nums[i] += 1
		else: 
			nums[i] = 1

nums = sorted(list(i) for i in nums.items())

min_poly = ''

i = 0
for k,v in nums:
	if k != '0' and v >=2:
		min_poly += k
		nums[i][1] -= 2
		break
	i += 1

# print(nums)
min_num = '9'
min_num_flag = 0

for k, v in nums: 
	while v >= 2 and min_poly: 
		min_poly += k
		v -= 2
	if v == 1: 
		if k <= min_num: 
			min_num = k
			min_num_flag = 1

print(min_poly, min_num if min_num_flag else '', min_poly[::-1], sep='')