# n = int(input()) 
arr = list("1 2 3 4 5".split()) 

for i in range(1, len(arr)-1, 2): 
	print(arr[i], arr[i-1], end=' ')

if len(arr)%2 == 1: print(arr[-1])
