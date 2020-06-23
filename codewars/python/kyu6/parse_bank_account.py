# https://www.codewars.com/kata/597eeb0136f4ae84f9000001

def parse_num(i, bank_account):

	num_list = [
		[[0, 1, 0],
		 [1, 0, 1],
		 [1, 1, 1]], # 0
		[[0, 0, 0],
		 [0, 0, 1],
		 [0, 0, 1]], # 1
		[[0, 1, 0],
		 [0, 1, 1],
		 [1, 1, 0]], # 2
		[[0, 1, 0],
		 [0, 1, 1],
		 [0, 1, 1]], # 3
		[[0, 0, 0],
		 [1, 1, 1],
		 [0, 0, 1]], # 4
		[[0, 1, 0],
		 [1, 1, 0],
		 [0, 1, 1]], # 5
		[[0, 1, 0],
		 [1, 1, 0],
		 [1, 1, 1]], # 6
		[[0, 1, 0],
		 [0, 0, 1],
		 [0, 0, 1]], # 7
		[[0, 1, 0],
		 [1, 1, 1],
		 [1, 1, 1]], # 8
		[[0, 1, 0],
		 [1, 1, 1],
		 [0, 1, 1]], # 9
	]

	row = 0
	num = []
	while row <= 2:
		row_list = []
		col = 0
		while col <= 2:
			row_list.append(1 if bank_account[row][col + i] !=  ' ' else 0)
			col += 1
		num.append(row_list)
		row += 1

	return num_list.index(num)


def parse_bank_account(bank_account):
    bank_account = bank_account.split('\n')
    # print(bank_account)

    i = 0
    res = 0
    while i <= len(bank_account[0]) - 2:
        res = parse_num(i, bank_account) + res * 10
        i += 3

    return res


text =  ' _  _  _  _  _  _  _  _  _  _  _ \n'+ \
		'|_| _| _||_||_ |_ |_ |_ |_||_||_|\n'+ \
		'|_||_  _||_| _| _| _||_| _||_| _|\n'

print(parse_bank_account(text))