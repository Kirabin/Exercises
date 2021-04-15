# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

def bouncingBall(h, bounce, window):

	if (not 0 < bounce < 1
		or h <= 0
		or window >= h):
		return -1

	bounces = -1
	while h > window:
		h *= bounce
		bounces += 2

	return bounces


assert bouncingBall(3, 0.66, 1.5) == 3
assert bouncingBall(30, 0.66, 1.5) == 15
assert bouncingBall(2, 0.5, 1) == 1 