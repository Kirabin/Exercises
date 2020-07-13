DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = 12, 30 or map(int, input().split())
month -= 1

day_till = sum(DAYS[month+1:]) + DAYS[month] - day
print(day_till)