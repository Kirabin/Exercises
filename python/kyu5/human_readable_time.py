# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):

	hh = seconds // (60*60)
	mm = seconds // 60 % 60
	ss = seconds % 60

	return f"{hh:02}:{mm:02}:{ss:02}"




assert make_readable(0) == "00:00:00"
assert make_readable(5) == "00:00:05"
assert make_readable(60) == "00:01:00"
assert make_readable(86399) == "23:59:59"
assert make_readable(359999) == "99:59:59"