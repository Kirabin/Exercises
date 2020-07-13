n = int(input())
arr = input().split()
print(' '.join(arr[:len(arr)//2][::-1]), ' '.join(arr[len(arr)//2:][::-1]))
# print(arr_rev)