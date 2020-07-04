# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

def count_smileys(arr):

	res = 0
	for i in arr:
		if len(i) == 3:
			if i[1] not in "-~":
				continue

		if (i[0] not in ":;" or
			i[-1] not in ")D"):
			continue

		res += 1

	return res


# Other's answer
# from re import findall
# def count_smileys(arr):
	# return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


assert count_smileys([]) == 0
assert count_smileys([':D', ':~)', ';~D', ':)']) == 4
assert count_smileys([':)', ':(', ':D', ':O', ':;']) == 2
assert count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1
