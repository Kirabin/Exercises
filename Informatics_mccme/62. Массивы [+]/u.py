import random 

start, end, n = 10, 20, 10
arr = [random.randint(start, end) for i in range(n)]
print(' '.join(map(str, arr)))


max_sum = 0
max_index = 0
for i in range(n//2):
	el_sum = arr[i] + arr[-i-1]

	if el_sum%2 == 0 and el_sum > max_sum:
		max_sum = el_sum
		max_index = i

print(max_index+1, n - max_index)