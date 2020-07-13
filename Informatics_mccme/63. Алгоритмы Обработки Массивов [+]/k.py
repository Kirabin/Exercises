n = int('6') 
arr = '1 2 3 4 5 6'.split()
start, stop = 2, 5
print(' '.join(sum([arr[:start-1], arr[start-1:stop][::-1], arr[stop:]], [])))