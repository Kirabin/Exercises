opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}

def dirReduc(arr):
    path = []

    for i in arr: 
        if path and path[-1] == opposite[i]:
            path.pop()
        else:
            path.append(i)
    
    return path

    
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# a = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(a))