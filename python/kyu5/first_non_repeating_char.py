# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

from collections import Counter


def first_non_repeating_letter(string):
	c = Counter(string.lower())

	for i in string:
		if c[i.lower()] == 1:
			return i

	return ''


assert first_non_repeating_letter('a') == 'a'
assert first_non_repeating_letter('stress') == 't'
assert first_non_repeating_letter('moonmen') == 'e'

assert first_non_repeating_letter('') == ''

assert first_non_repeating_letter('abba') == ''
assert first_non_repeating_letter('aa') == ''

assert first_non_repeating_letter('~><#~><') == '#'
assert first_non_repeating_letter('hello world == eh?') == 'w'

assert first_non_repeating_letter('sTreSS') == 'T'
assert first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ','