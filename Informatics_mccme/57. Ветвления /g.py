DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a = 13 or int(input())
print(DAYS[a] if 0 <= a <= 11 else 0)