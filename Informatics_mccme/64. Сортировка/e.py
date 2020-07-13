n = int(input())
arr = list(map(int, input().split())) 

flag = 1
for i in range(n): 
	for j in range(1, n-i): 

		if arr[j-1] > arr[j]: 
			arr[j-1], arr[j] = arr[j], arr[j-1]
			flag = 0
			print(' '.join([str(i) for i in arr]))

if flag: 
	print(0)