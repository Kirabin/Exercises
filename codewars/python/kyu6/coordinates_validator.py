# https://www.codewars.com/kata/5269452810342858ec000951/train/python

import re


def is_valid_coordinates(coordinates):
	pattern = r"\-?(\d*\.?\d*), \-?(\d*\.?\d*)"

	res = re.fullmatch(pattern, coordinates)

	if (not res or
		not float(res.group(1)) <= 90 or
		not float(res.group(2)) <= 180):
		return False

	return True


valid_coordinates = [
	"-23, 25",
	"4, -3",
	"24.53525235, 23.45235",
	"04, -23.234235",
	"43.91343345, 143"
]

for coordinate in valid_coordinates:
	assert is_valid_coordinates(coordinate) is True


invalid_coordinates = [
	"23.234, - 23.4234",
	"2342.43536, 34.324236",
	"N23.43345, E32.6457",
	"99.234, 12.324",
	"6.325624, 43.34345.345",
	"0, 1,2",
	"0.342q0832, 1.2324",
	"23.245, 1e1"
]

for coordinate in invalid_coordinates:
	assert is_valid_coordinates(coordinate) is False
