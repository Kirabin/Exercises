# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def countBits(n):

    return bin(n)[2:].count('1')


assert countBits(0) == 0
assert countBits(4) == 1
assert countBits(7) == 3
assert countBits(9) == 2
assert countBits(10) == 2
