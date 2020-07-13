# start, stop, goals_needed = map(int, input().split())

n = int(input())

persons = []
max_goals = 0
max_goals_count = 1
for i in range(n): 
	last_name, first_name, year, goals = input().split()
	
	goals = int(goals)
	if goals > max_goals: 
		persons = [last_name + ' ' + first_name]
		max_goals = goals
		max_goals_count = 1
	elif goals == max_goals: 
		persons.append(last_name + ' ' + first_name)
		max_goals_count += 1

print('\n'.join(persons))
print(max_goals)