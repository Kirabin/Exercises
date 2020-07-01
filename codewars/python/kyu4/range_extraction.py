# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
# 971
def solution(args):

	res = []
	i = 0
	while i < len(args) :
		j = 1
		while i + j < len(args) and args[i + j] == args[i] + j:
			j += 1

		if j > 2: 
			res.append(f"{args[i]}-{args[i + j - 1]}")
		else:
			res.append(f"{args[i]}")

		i += j if j > 2 else 1

	return ",".join(res)



assert solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
assert solution([-3,-2,-1,2,10,15,16,18,19,20]) == '-3--1,2,10,15,16,18-20'