n = int(input())

l = []
for i in range(n): 
	trash ,d = input().split()
	l.append(d)

for i, s in enumerate(sorted(l), 1): 
	print(f"{i}. {s}")
