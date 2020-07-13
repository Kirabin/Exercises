l = []
while 1:
	d = input().split()
	if d: 
		l.append(d[1])
	else: 
		break

for i, s in enumerate(sorted(l), 1): 
	print(f"{i}. {s}")
