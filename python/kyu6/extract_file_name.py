# https://www.codewars.com/kata/597770e98b4b340e5b000071/train/python

import re


class FileNameExtractor:
	def extract_file_name(dirty_file_name):
		pattern = r"\d*_([\w-]+\.[\w-]+)"

		res = re.search(pattern, dirty_file_name)
		return res.group(1)


assert FileNameExtractor.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION") == "FILE_NAME.EXTENSION"
assert FileNameExtractor.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34") == "FILE_NAME.EXTENSION"
