# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

from collections import Counter

def anagrams(word, words):
	return [i for i in words if Counter(i) == Counter(word)]

assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']