inp = 9 or int(input()) 

arr = [str(2**i) for i in range(2, inp, 2)]
print(' '.join(arr[::-1]))