# 17 / 25

n = int(input()) 
arr = list(map(int, input().split())) 

save_max_num = -1 
max_num = -1 
arr.sort()
for i in arr: 
	if i > max_num: 
		max_num = i
	elif i == max_num: 
		save_max_num = max_num

print(save_max_num)