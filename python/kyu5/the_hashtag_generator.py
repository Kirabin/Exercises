# https://www.codewars.com/kata/52449b062fb80683ec000024/python

def generate_hashtag(s):
	res = '#'

	for i in s.split():
		res += i.capitalize()

	if len(res) > 141 or len(res) == 1:
		return False

	return res


assert generate_hashtag('') is False  # 'Expected an empty string to return False'
assert generate_hashtag('Do We have A Hashtag')[0] == '#'   # 'Expeted a Hashtag (#) at the beginning.'
assert generate_hashtag('Codewars') == '#Codewars'  # 'Should handle a single word.'
assert generate_hashtag('Codewars      ') == '#Codewars'  # 'Should handle trailing whitespace.'
assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'  # 'Should remove spaces.'
assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'  # 'Should capitalize first letters of words.'
assert generate_hashtag('CodeWars is nice') == '#CodewarsIsNice'  # 'Should capitalize all letters of words - all lower case but the first.'
assert generate_hashtag('c i n') == '#CIN'  # 'Should capitalize first letters of words even when single letters.'
assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'  # 'Should deal with unnecessary middle spaces.'
assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') is False  # 'Should return False if the final word is longer than 140 chars.'
