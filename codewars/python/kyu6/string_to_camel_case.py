# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
	
	text = text.replace("-", "_")
	res = [i.capitalize() for i in text.split("_")]

	if text:
		return text[0] + "".join(res)[1:]
	else: 
		return ""


print(to_camel_case("the-stealth-warrior"))