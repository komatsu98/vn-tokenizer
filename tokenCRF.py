from tokenization.crf_tokenizer import CrfTokenizer
from tokenization.base_tokenizer import BaseTokenizer

crf_tokenizer_obj = CrfTokenizer()
# crf_tokenizer_obj.train('data/tokenized/samples/training')
# Note: If you trained your model, please set correct model path and do not train again!
crf_tokenizer_obj = CrfTokenizer(model_path='models/pretrained_tokenizer.crfsuite')

import xlrd
import time
import re

partern = re.compile("[0-9a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ\s]+")

wordFreqs = []
totalLength = 0
start = time.time()
words = {
	0: {},
	1: {},
	2: {},
	3: {}
}

f = open("tokenization/stopwords.txt", "r")
stop_words = f.read().split("\n")
f.close()
f = open("tokenization/cus_stopwords.txt", "r")
stop_words = stop_words + f.read().split("\n")
f.close()

# # social 
# workbook = xlrd.open_workbook('data/test/social.xls')
# print('data/test/social.xls')
# sheet = workbook.sheet_by_index(0)
# columns = [3]
# row_start = 2

# ifollow 
workbook = xlrd.open_workbook('data/test/ifollow.xls')
print('data/test/ifollow.xls')
sheet = workbook.sheet_by_index(0)
columns = [3, 5, 7]
row_start = 9

for c in columns: 
	for r in range(row_start, sheet.nrows):
		content = sheet.cell_value(r, c)
		totalLength += len(content)

		# test time for half file
		# if totalLength > 50000:
		# 	break
		
		tokenized = crf_tokenizer_obj.get_tokenized(content).lower()
		tokenized = tokenized.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=-+'"}).split(" ")
		for word in tokenized:
			word = word.replace("_", " ").strip()
			if len(word) == 1 or word in stop_words or (word.isnumeric() and int(word) < 100) or not bool(partern.match(word)):
				continue

			if word in words[0]:
				words[0][word] += 1
			else: 
				words[0][word] = 1

			for length in range(3):
				if(len(word.split(" ")) == length + 1):
					if word in words[length+1]:
						words[length+1][word] += 1
					else: 
						words[length+1][word] = 1

end = time.time()
print("length", totalLength)
print("time", end - start)

word_list_1 = words[1].keys()
word_list_2 = words[2].keys()
word_list_3 = words[3].keys()

for length in range(4):
	# sort
	words[length] = {k: v for k, v in sorted(words[length].items(), key=lambda item: item[1], reverse=True)}
	iwords = iter(words[length])
	f = open(f"top_word_CRF_{length}.txt", "w")
	out = ""
	i = 0
	for key in iwords:
		if i > 99: break
		i += 1
		out += f"#{i}. {key} x{words[length][key]}\n"
	f.write(out)
	f.close()
