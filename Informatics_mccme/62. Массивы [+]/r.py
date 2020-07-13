import random 
a = 10 or int(input())
b = [str(i) for i in range(1, a+1) if i != 5] 
random.shuffle(b)
print(5, " ".join(b))