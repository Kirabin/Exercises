a = 12345 or int(input()) 

units = map(int, str(a))
count = 0
for i in units: 
	if i%2 == 0: 
		count += 1

print(count)