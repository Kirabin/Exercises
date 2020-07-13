# there's only this found
# stupid task (won't make you any smarter)

s = """
6,
28,
496,
8128,
33 550 336,
8 589 869 056,
137 438 691 328,
2 305 843 008 139 952 128,
2 658 455 991 569 831 744 654 692 615 953 842 176,
191 561 942 608 236 107 294 793 378 084 303 638 130 997 321 548 169 216
"""

n = 

perfect_numbers = []
s2 = ''
for i in s.split():
	s2 += i
s = s2

perfect_numbers = list(map(int, s.split(',')))
print(perfect_numbers)
