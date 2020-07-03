# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python

from collections import Counter
from string import ascii_lowercase as loweralpha

def mix(s1, s2):

	counter_s1 = Counter([i for i in s1 if i in loweralpha])
	counter_s2 = Counter([i for i in s2 if i in loweralpha])

	most_frequest = {}
	for (letter, count_1, count_2) \
	in [(i, counter_s1[i], counter_s2[i]) for i in loweralpha]:
		if count_1 > count_2:
			if count_1 > 1:
				most_frequest[letter] = ('1', count_1)
		elif count_1 < count_2:
			if count_2 > 1:
				most_frequest[letter] = ('2', count_2)
		else: 
			if count_1 > 1:
				most_frequest[letter] = ('=', count_1)

	res = []
	for letter, (of_string, amount) in sorted(most_frequest.items(), key = lambda x: (x[1][1], "=21".index(x[1][0]), -ord(x[0])), reverse = True):
		res.append(f"{of_string}:{letter*amount}")

	return "/".join(res)


assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"
assert mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
assert mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"
assert mix("codewars", "codewars") == ""
assert mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"