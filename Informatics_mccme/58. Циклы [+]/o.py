inp = '1422' or input()
a = set(i for i in inp)
if len(a) < len(inp):
	print('YES')
else:
	print('No')