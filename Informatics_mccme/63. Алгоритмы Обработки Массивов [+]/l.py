n = int('6') 
arr = '1 2 3 4 5 6'.split()
shift = 2
print(' '.join(sum([arr[shift:], arr[:shift]], [])))