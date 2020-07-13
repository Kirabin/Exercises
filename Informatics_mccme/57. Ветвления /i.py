x, y = 1, 0.5 or map(float, input().split()) 

bit_str = ''
bit_str += '1' if y < 1 else '0'
bit_str += '1' if y+x < 0 else '0'
bit_str += '1' if x**2 + y**2 < 1 else '0'
bit_str += '1' if (x-1)**2 + y**2 < 1 else '0'

print(bit_str)