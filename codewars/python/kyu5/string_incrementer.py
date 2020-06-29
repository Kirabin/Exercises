# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def increment_string_too_complex(string):

	numeral_part = ""
	pos = -1
	for i in range(1, len(string) + 1):
		if pos == -1:
			if string[-i] in "0123456789": 
				numeral_part = string[-i] + numeral_part
			else:
				pos = -i
				break

	lateral_part = string[:] if not numeral_part else string[:pos+1]
	leading_zeroes = len(numeral_part) - len(numeral_part.lstrip('0'))
	numeral_part = numeral_part[leading_zeroes:]

	try: 
		new_numeral_part = str(int(numeral_part) + 1)
	except:
		new_numeral_part = "1"

	res = f"{lateral_part}" + \
		  f"{'0'*(leading_zeroes - len(new_numeral_part) + len(numeral_part))}" + \
		  f"{new_numeral_part}"

	print(res)
	return res

def increment_string(string):
	head = string.rstrip("0123456789")
	tail = string[len(head):]
	if not tail: 
		return head + "1"
	return f"{head}{int(tail) + 1:0{len(tail)}}"


assert increment_string("009009") == "009010"
assert increment_string("foo") == "foo1"
assert increment_string("foob000ar001") == "foob000ar002"
assert increment_string("foobar1") == "foobar2"
assert increment_string("foobar00") == "foobar01"
assert increment_string("foobar99") == "foobar100"
assert increment_string("foobar099") == "foobar100"
assert increment_string("") == "1"