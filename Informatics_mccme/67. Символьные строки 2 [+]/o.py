inp = input()

nums = {}
for i in inp: 
	if '0' <= i <= '9':
		if i in nums: 
			nums[i] += 1
		else: 
			nums[i] = 1

# print(nums)
nums =  sorted(nums.items()) 

for i, v in sorted(nums, key = lambda x: x[1]):
	print(i, end='')
