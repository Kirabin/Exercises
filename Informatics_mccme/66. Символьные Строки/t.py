rim_nums = {'I': 1, 
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500, 
			'M': 1000}

def from_rim(s): #string
	# global rim_nums
	if not s: return 0

	num = rim_nums[s[-1]]
	for i in range(len(s)-1):
		right = rim_nums[s[-i-1]]
		left = rim_nums[s[-i-2]] 
		if right <= left: 
			num += left
		else: 
			num -= left
	return num 

def to_rim(a): 
	if a > 5999: return 0

	rim_str = ''	

	d = 0 
	chars = ['']
	chars.extend(rim_nums.keys())
	chars.extend(['',''])
	for i in map(int, str(a)[::-1]):
		template = [ '',
					 chars[1+d],
					 chars[1+d]*2,
					 chars[1+d]*3, 
					 chars[1+d] + chars[2+d],
					 chars[2+d],
					 chars[2+d] + chars[1+d],
					 chars[2+d] + chars[1+d]*2,
					 chars[2+d] + chars[1+d]*3, 
					 chars[1+d] + chars[3+d]]
		if d == 6 : 
			template[i] = 'M'*(a//1000)

		rim_str = template[i] + rim_str
		d += 2

	return rim_str

rim_str = 'MCMLXIX'
print(from_rim(rim_str))
