from itertools import permutations as perm

def permutations(string):
	return set("".join(p) for p in perm(string))
	

assert sorted(permutations('a')) == ['a']
assert sorted(permutations('ab')) == ['ab', 'ba']
assert sorted(permutations('aabb')) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']