# https://www.codewars.com/kata/52e1476c8147a7547a000811/solutions/python

# My take
regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{6,}$"


# [a-zA-Z0-9] == \w

# Other's solutions
# regex = (
#     '^'            # start line
#     '(?=.*\d)'     # must contain one digit from 0-9
#     '(?=.*[a-z])'  # must contain one lowercase characters
#     '(?=.*[A-Z])'  # must contain one uppercase characters
#     '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
#     '{6,}'         # length at least 6 chars
#     '$'            # end line
# )
