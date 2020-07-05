# https://www.codewars.com/kata/550554fd08b86f84fe000a58

def in_array(array1, array2):

	res = []
	for i in set(array1): 
		for j in array2: 
			if i in j:
				res.append(i)
				break

	return sorted(res)


a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
assert in_array(a1, a2) == r