# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

def sum_pairs_non_efficient(ints, s):

	i = 0 
	pair = []
	min_pair_j = len(ints)
	for i in range(len(ints)-1):

		for j in range(i + 1, len(ints)):

			if ints[i] + ints[j] == s:
				if j < min_pair_j:
					min_pair_j = j
					pair = [ints[i], ints[j]]
					print(pair)


	return pair or None



def sum_pairs(ints, s): 

	hash_table = set()   
	for i in ints: 
		if s - i in hash_table: # complexity of 'value' in set is O(1)
			return [s - i, i]
		hash_table.add(i)

	# if there's no return stetaments python returns None
	# return None 




assert sum_pairs([0, 0, -2, 3], 2) == None
assert sum_pairs([5, 4, 5], 10) == [5, 5]
assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7]