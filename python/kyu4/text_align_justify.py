# https://www.codewars.com/kata/537e18b6147aa838f600001b

from math import ceil

def justify(text, width):

	res = []
	words = text.split()

	i = 0
	while i < len(words):
		len_line = 0  # len with 1 space
		line = []
		while len_line + len(words[i]) <= width:
			len_line += len(words[i]) + 1
			line.append(words[i])
			i += 1
			if i >= len(words):
				break

		if i == len(words) or len(line) == 1:
			res_line = " ".join(line)
		else:
			spaces_whole = width - sum(len(i) for i in line)

			spaces = []
			while spaces_whole:
				temp = ceil(spaces_whole / (len(line) - len(spaces) - 1))
				spaces.append(" "*temp)
				spaces_whole -= temp


			res_line = "".join(word + s for s, word in zip(spaces, line)) + line[-1]

		res.append(res_line)

	print("\n".join(res))
	print()
	return "\n".join(res)


assert justify("a a a a a a a aaaaaaaaaaaaa", 17)
assert justify("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.", 30)

assert justify('123 45 6', 7) == '123  45\n6'
assert justify('123 45', 7) == '123 45'
assert justify('123 4567 34', 12) == '123 4567 34'
