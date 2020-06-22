# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(array):
    non_zero_arr = []
    zero_arr = []
    
    for i in array:
        if (type(i) == int or type(i) == float) and i in [0, 0.0]:  
            zero_arr.append(0)
        else:
            non_zero_arr.append(i)
    
    return non_zero_arr + zero_arr




assert	move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == \
		[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
		