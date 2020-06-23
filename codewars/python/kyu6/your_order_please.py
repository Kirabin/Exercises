# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def get_num(s):

	for i in s:
		if i in "0123456789":
			return int(i)

	return -1


def order(sentence):

	res = sentence.split()

	d_res = [(i, get_num(i)) for i in res]

	d_res.sort(key = lambda x: x[1])

	return ' '.join([i[0] for i in d_res])



assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
assert order("") ==  ""