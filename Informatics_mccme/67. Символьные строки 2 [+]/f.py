l = []
while 1:
	d = input().split()
	if d: 
		l.append((d[0], d[1]))
	else: 
		break

for i, p in enumerate(sorted(l, key=lambda person: person[1]), 1): 
	print(f"{i}. {p[0]} {p[1]}")
