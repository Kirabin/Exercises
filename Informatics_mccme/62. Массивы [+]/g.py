start, step, steps = 5, 3, 6 or map(int, input().split())
print(" ".join([str(i*step+start) for i in range(steps)][::-1]))