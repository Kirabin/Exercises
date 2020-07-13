import random 

start, end, n = 10, 100, 10 or map(int, input().split())

arr = [random.randint(start, end) for i in range(n)]
print(' '.join(map(str, arr)))

min_range = abs(arr[0] - arr[1])
min_index_one, min_index_two = 0, 1
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if abs(arr[i]-arr[j]) < min_range:
			min_index_one = i
			min_index_two = j
			min_range = abs(arr[i]-arr[j])

print(min_index_one+1, min_index_two+1)