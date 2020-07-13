n = int(input())
arr = list(map(int, input().split())) 

print(' '.join([str(i) for i in sorted(arr)]))
print(len(set(arr)))