# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/python

def find_even_index(arr):
    left_sum = 0
    right_sum = sum(arr)
    
    
    for i, a in enumerate(arr):
        right_sum -= a
        if left_sum == right_sum: 
            return i
        left_sum += a
    

    return -1 

a = find_even_index([1,2,3,4,3,2,1])
print(a)