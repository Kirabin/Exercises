# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python


def pig_it(text):

	new_words = []
	for word in text.split(" "):
		if word in list(".!,?"):
			new_words.append(word)
		else:
			new_words.append(word[1:] + word[:1] + "ay")

	return ' '.join(new_words)



assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert pig_it('This is my string') == 'hisTay siay ymay tringsay'