# https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

def decrypt(encrypted_text, n):

	l = len(encrypted_text) if encrypted_text else 0
	for _ in range(n):
		encrypted_text = "".join([j + i for i, j in zip(encrypted_text[:l//2], encrypted_text[l//2:])]) \
						 +  (encrypted_text[-1] if l % 2 == 1 else "")

	return encrypted_text


def encrypt(text, n):

	for _ in range(n):
		text = text[1::2] + text[::2]

	return text



assert encrypt("This is a test!", 0) == "This is a test!"
assert encrypt("This is a test!", 1) == "hsi  etTi sats!"
assert encrypt("This is a test!", 2) == "s eT ashi tist!"
assert encrypt("This is a test!", 3) == " Tah itse sits!"
assert encrypt("This is a test!", 4) == "This is a test!"
assert encrypt("This is a test!", -1) == "This is a test!"
assert encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig"

assert decrypt("This is a test!", 0) == "This is a test!"
assert decrypt("hsi  etTi sats!", 1) == "This is a test!"
assert decrypt("s eT ashi tist!", 2) == "This is a test!"
assert decrypt(" Tah itse sits!", 3) == "This is a test!"
assert decrypt("This is a test!", 4) == "This is a test!"
assert decrypt("This is a test!", -1) == "This is a test!"
assert decrypt("hskt svr neetn!Ti aai eyitrsig", 1) == "This kata is very interesting!"

assert encrypt("", 0) == ""
assert decrypt("", 0) == ""
assert encrypt(None, 0) == None
assert decrypt(None, 0) == None