def solution(s):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""


    word = ""
    for i in s + 'A':  
    	if i in alphabet_upper:
    		res += word + " "
    		word = ""
    	word += i

    return res[:-1]


def testing():
	tests = {
		"helloWorld": "hello World",
		"breakCamelCase": "break Camel Case"
	}

	for test, answer in tests.items():
		my_answer = solution(test)
		print(f"{test}: {answer}")
		print(my_answer)
		print('OK' if my_answer == answer else "FAIL")
		print()



testing()