n = int('6') 
arr = '1 2 3 4 5 6'.split()
start, stop = 0, n
shift = 2
print(' '.join(sum([arr[-shift:],
					arr[:-shift]], 
				   [])))