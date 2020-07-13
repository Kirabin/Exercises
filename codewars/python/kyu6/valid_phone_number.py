# https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python

import re


def validPhoneNumber(phoneNumber):
	res = re.search("^\(\d{3}\) \d{3}-\d{4}$", phoneNumber)
	return res is not None


assert validPhoneNumber("(123) 456 7890") is False
assert validPhoneNumber("(123) 456-7890") is True
