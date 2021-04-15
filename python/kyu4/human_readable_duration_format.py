# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):

	if seconds == 0:
		return "now"

	y, seconds = divmod(seconds, 3600 * 24 * 365)
	d, seconds = divmod(seconds, 3600 * 24)
	h, seconds = divmod(seconds, 3600)
	m, seconds = divmod(seconds, 60)
	s = seconds

	res = []

	if y == 1:
		res.append(f"{y} year")
	elif y > 1:
		res.append(f"{y} years")

	if d == 1:
		res.append(f"{d} day")
	elif d > 1:
		res.append(f"{d} days")

	if h == 1:
		res.append(f"{h} hour")
	elif h > 1:
		res.append(f"{h} hours")

	if m == 1:
		res.append(f"{m} minute")
	elif m > 1:
		res.append(f"{m} minutes")

	if s == 1:
		res.append(f"{s} second")
	elif s > 1:
		res.append(f"{s} seconds")

	res = ", ".join(res[:-1]) + (" and " if len(res) >= 2 else "") + res[-1]
	return res


assert format_duration(1) == "1 second"
assert format_duration(62) == "1 minute and 2 seconds"
assert format_duration(120) == "2 minutes"
assert format_duration(3600) == "1 hour"
assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"