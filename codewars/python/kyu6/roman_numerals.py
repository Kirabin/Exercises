# "to_rim" https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
# "from_rim" https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

rim_nums = {'I': 1, 
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500, 
			'M': 1000}


def from_rim(s):
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


assert from_rim('XXI') == 21
assert from_rim('I') == 1
assert from_rim('IV') == 4
assert from_rim('MMVIII') == 2008
assert from_rim('MDCLXVI') == 1666
assert from_rim('MCMLXIX') == 1969

assert to_rim(1) == 'I'
assert to_rim(4),'IV'
assert to_rim(6),'VI'
assert to_rim(14),'XIV'
assert to_rim(21),'XXI'
assert to_rim(89),'LXXXIX'
assert to_rim(91),'XCI'
assert to_rim(984),'CMLXXXIV'
assert to_rim(1000), 'M'
assert to_rim(1889),'MDCCCLXXXIX'
assert to_rim(1989),'MCMLXXXIX'