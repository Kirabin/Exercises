start, step, steps = 8, 4, 5 or map(int, input().split())
print(" ".join([str(i*step+start) for i in range(steps)]))