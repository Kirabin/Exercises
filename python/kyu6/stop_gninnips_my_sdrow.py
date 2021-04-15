# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):

	new_sen = []
	for i in sentence.split(' '):
		if len(i) >= 5: 
			new_sen.append(i[::-1])
		else:
			new_sen.append(i)

	return " ".join(new_sen)



assert spin_words( "Hey fellow warriors" ) == "Hey wollef sroirraw" 
assert spin_words( "This is a test") == "This is a test" 
assert spin_words( "This is another test" )== "This is rehtona test"