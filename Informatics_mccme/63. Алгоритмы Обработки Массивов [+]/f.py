n = int("6")
arr = list(map(int, "1 2 3 4 0 5".split())) 

arr.sort()
for i in arr[:3]: print(i, end=' ')