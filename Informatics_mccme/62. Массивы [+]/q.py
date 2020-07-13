import random 
a = 10 or int(input())
b = [str(i) for i in range(1, a+1)] 
random.shuffle(b)
print(" ".join(b))