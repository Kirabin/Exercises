# https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python

def namelist(names):

	if not names: 
		return ""
	if len(names) == 1:
		return names[0]['name']

	return ", ".join([i['name'] for i in names][:-1]) + " & " + names[-1]['name']


assert namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge'
assert namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie'
assert namelist([{'name': 'Bart'},{'name': 'Lisa'}]) == 'Bart & Lisa'
assert namelist([{'name': 'Bart'}]) == 'Bart'
assert namelist([]) == ''