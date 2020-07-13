def digit_sum(num): 
	return sum(map(int, str(num)))

n = int(input()) 
arr = list(map(int, input().split())) 

arr.sort(key= lambda x: digit_sum(x), reverse=True)
print(' '.join([str(i) for i in arr]))