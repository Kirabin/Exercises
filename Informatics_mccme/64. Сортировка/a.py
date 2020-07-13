n = int(input())
arr = input().split()

print(' '.join(sorted(arr, key = lambda x: x[-1])))