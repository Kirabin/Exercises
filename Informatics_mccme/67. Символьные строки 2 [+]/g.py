start, stop, goals_needed = map(int, input().split())

n = int(input())

count = 0
for i in range(n): 
	last_name, first_name, year, goals = input().split()
	if start <= int(year) <= stop and int(goals) == goals_needed: 
		print(last_name, first_name)
		count += 1

print(count)