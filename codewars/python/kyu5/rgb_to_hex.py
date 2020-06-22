def to_hex(a):
	a = max(0, a)
	a = min(255, a)
	a = hex(a)[2:].upper()

	return a if len(a) == 2 else '0' + a


def rgb(r, g, b):

	return to_hex(r) + to_hex(g) + to_hex(b)
	


assert rgb(255,255,255) == "FFFFFF"
assert rgb(255,255,300) == "FFFFFF"
assert rgb(255,255,-1)  == "FFFF00"
assert rgb(-20,275,125) == "00FF7D"


