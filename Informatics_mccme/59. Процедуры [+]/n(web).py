# Dunno, better solve something useful


# from wiki, edited from c#
# works fine 
def to_negabinary(a):

	res = ''
	while a != 0: 
		remainder = a % -2;
		a //= -2

		if remainder < 0: 
			remainder += 2
			a += 1

		res = str(remainder) + res

	return res

print(to_negabinary(-12))