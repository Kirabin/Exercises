# https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
	res = url.split('//')[-1]

	for i in res.split('.'):
		if i != "www":
			return i
	
print(domain_name("http://www.sgoogle.co.jp"))