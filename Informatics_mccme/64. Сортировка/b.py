n = int(input())
arr = list(map(int, input().split())) 

min_arr = sorted(arr)[:3]

for i in min_arr: print(i, end=' ') 

for i in arr: 
	if i in min_arr: 
		del min_arr[min_arr.index(i)]
		continue
	else: 
		print(i, end=' ') 