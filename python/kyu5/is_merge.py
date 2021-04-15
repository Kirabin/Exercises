# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python

def is_merge(s, part1, part2):

	if not s and not part1 and not part2:
		return 1
	elif not s:
		return 0

	if (part1 and part2 and 
		part1[0] == s[0] and part2[0] == s[0]):
		return is_merge(s[1:], part1[1:], part2) or is_merge(s[1:], part1, part2[1:])
	elif part1 and part1[0] == s [0]:
		return is_merge(s[1:], part1[1:], part2)
	elif part2 and part2[0] == s [0]:
		return is_merge(s[1:], part1, part2[1:])
	return 0



assert is_merge('codewars', 'code', 'wars')
assert is_merge('codewars', 'cdw', 'oears')
assert not is_merge('codewars', 'cod', 'wars')