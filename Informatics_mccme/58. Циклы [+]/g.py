a, b = 133, 125 or map(int, input().split())
c, d = 134, 111 or map(int, input().split())

for i in range(10000, 100000): 
	if i%a == b and i%c == d: 
		print(i, end=' ')