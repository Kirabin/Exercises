a, b = 6,4 or map(int, input().split())
print(" ".join([str(i+a) for i in range(b)][::-1]))