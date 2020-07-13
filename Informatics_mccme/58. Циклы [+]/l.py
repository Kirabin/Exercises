a = 12345 or int(input()) 

units = map(int, str(a))
count = 0
for i in units: 
	count += i

print(count)