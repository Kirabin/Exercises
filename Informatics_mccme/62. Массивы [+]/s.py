import random

start, end, n = 10, 20, 10 or map(int, input().split()) 

first_num, second_num = 0, random.randint(start, end)
min_sum = 20000
index = 1
min_index = 1
print(second_num, end=' ')
for i in range(n): 
	first_num, second_num = second_num, random.randint(start, end)

	if first_num + second_num <= min_sum: 
		min_index = index 
		min_sum = first_num + second_num
	print(second_num, end=' ')
	index += 1 

print()
print(min_index, min_index+1)