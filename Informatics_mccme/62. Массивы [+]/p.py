import random 

start, end, n = -10, -1, 7 or map(int, input().split())

num_sum_one = 0
amount_one = 0
num_sum_two = 0
amount_two = 0
for i in range(n):
	a = random.randint(start, end)
	if a < 50: 
		num_sum_one += a
		amount_one += 1
	else: 
		num_sum_two += a
		amount_two += 1

	print(a, end=' ')

print()
ar_sum_one = 0 if amount_one == 0 else num_sum_one/amount_one
ar_sum_two = 0 if amount_two == 0 else num_sum_two/amount_twob
print("%.3f %.3f" % (ar_sum_one, ar_sum_two))