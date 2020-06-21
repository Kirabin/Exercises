# https://www.codewars.com/kata/55c6126177c9441a570000cc

def weight(a):
	w = 0 

	while a != 0:
		w += a%10
		a //= 10

	return w


def order_weight(strng):
	l = list(map(int, strng.split()))

	l.sort(key = lambda x: (weight(x), str(x)))


	return " ".join(map(str,l))




inp = "2000 11 11 10003 22 123 1234000 44444444 9999"

res = order_weight(inp)

test = "11 11 2000 10003 22 123 1234000 44444444 9999"
if res != test:
	print("Doesn't work")
	print(res, "!=" ,test)
else:
	print(res)