n = int(6) 
arr = list(map(int, "1 2 3 4 5 6".split())) 

print(' '.join([str(i) for i in arr[::3]]))