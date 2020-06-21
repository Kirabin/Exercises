def string_letter_count(s):
	letters = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}

	s = s.lower()
	for i in s:
		if i in letters.keys():
			letters[i] += 1


	res = ""
	for letter, count in letters.items():
		if count > 0:
			res += str(count) + letter

	return res

def testing():
	tests = {
		"The quick brown fox jumps over the lazy dog.": "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z",
		"The time you enjoy wasting is not wasted time.": "2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y",
		"./4592#{}()": ""
	}

	for test, answer in tests.items():
		my_answer = string_letter_count(test)
		print(f"{test}: {answer}")
		print(my_answer)
		print('OK' if my_answer == answer else "FAIL")
		print()


testing()