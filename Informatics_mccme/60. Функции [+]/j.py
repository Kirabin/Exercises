def num_sum(a): 
        return sum(map(int, str(a)))

start, stop = map(int, input().split()) 
start = ((start-1)//9+1)*9

flag = 1
for i in range(start, stop+1, 9): 
        s = num_sum(i)
        for j in range(2, 9+1): 
                if s != num_sum(i*j):
                        break
        else:
                print(i, end=' ')
                flag = 0

if flag:
        print(0) 
