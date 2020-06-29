# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

def queue_time(customers, n):
	queues = [0 for i in range(n)]
	for i in customers:
		queues[queues.index(min(queues))] += i

	return max(queues)


assert queue_time([], 1) == 0
assert queue_time([5], 1) == 5
assert queue_time([2], 5) == 2
assert queue_time([1,2,3,4,5], 2) == 9
assert queue_time([1,2,3,4,5], 1) == 15 
assert queue_time([1,2,3,4,5], 100) == 5
assert queue_time([2,2,3,3,4,4], 2) == 9