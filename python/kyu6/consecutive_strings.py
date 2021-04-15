# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
	n = len(strarr)

	if n == 0 or k > n or k <= 0: 
		return ""

	max_len = 0
	max_pair = ""
	i = 0
	while i <= n - k: 

		pair = "".join(strarr[j] for j in range(i, i + k))

		# if (l := len(pair)) > max_len:
			# max_len = l

		if len(pair) > max_len:
			max_len = len(pair)
			max_pair = pair
		i += 1

	return max_pair





assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"
assert longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) == "oocccffuucccjjjkkkjyyyeehh"
assert longest_consec([], 3) == ""
assert longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
assert longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) == "wlwsasphmxxowiaxujylentrklctozmymu"
assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == ""
assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz"
assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15) == ""
assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0) == ""