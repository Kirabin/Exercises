n = int('7') or int(input()) 
arr = "1 1 1 3 2 2 2 2 1 1 1 3".split()

max_len = 1
max_len_elem = arr[0]
elem_len = 1


for i in range(1, len(arr)):
	if arr[i] == arr[i-1] and i != len(arr) -1 : 
		elem_len += 1
	else: 
		if elem_len > max_len: 
			max_len = elem_len 
			max_len_elem = arr[i-1]
		elem_len = 1

print(max_len_elem, max_len)