# https://www.codewars.com/kata/5263c6999e0f40dee200059d

# Didn't know itertools was so cool, I found better code for this kata:

from itertools import product

ADJACENT = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
	return ["".join(p) for p in product(*[ADJACENT[int(i)] for i in observed])]
	

# My first solution

# misses = {'1': [1, 2, 4],
# 		  '2': [1, 2, 3, 5],
# 		  '3': [2, 3, 6],
# 		  '4': [1, 4, 5, 7],
# 		  '5': [2, 4, 5, 6, 8],
# 		  '6': [3, 5, 6, 9],
# 		  '7': [4, 7, 8],
# 		  '8': [5, 7, 8, 9, 0],
# 		  '9': [6, 8, 9],
# 		  '0': [0, 8]}

# def get_combinations(possibles):
# 	sum_of_pos = sum([len(i) for i in possibles])
# 	positions = [0 for _ in range(len(possibles))]

# 	combinations = [positions[:]]
# 	while 1:
# 		nex = 1
# 		for i in range(len(possibles)): 
# 			nex, positions[i] = divmod(positions[i] + nex, len(possibles[i]))
# 		if nex == 1:
# 			break
# 		combinations.append(positions[:])

# 	return combinations


# def get_pins(observed):

# 	possibles = []
# 	for i in observed: 
# 		possibles.append(misses[i])

# 	res = []
# 	for i in get_combinations(possibles):
# 		combination = ""
# 		for j, pos in enumerate(i):
# 			combination += str(possibles[j][pos])

# 		res.append(combination)

# 	return res



assert sorted(get_pins('8')) == sorted(['5','7','8','9','0'])
assert sorted(get_pins('11')) == sorted(["11", "22", "44", "12", "21", "14", "41", "24", "42"])
assert sorted(get_pins('369')) == sorted(["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])