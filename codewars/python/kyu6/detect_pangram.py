# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

import string


def is_pangram(s):
    return all((i in set(s.lower())) for i in string.ascii_lowercase)


pangram = "The quick, brown fox jumps over the lazy dog!"
assert is_pangram(pangram) is True
