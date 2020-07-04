# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(sentence):

	max_score = 0
	max_score_word = ""
	for word in sentence.split():
		score = 0
		for i in word:
			score += ord(i) - ord('a') + 1

		if score > max_score:
			max_score = score
			max_score_word = word

	return max_score_word


assert high('man i need a taxi up to ubud') == 'taxi'
assert high('what time are we climbing up the volcano') == 'volcano'
assert high('take me to semynak') == 'semynak'
