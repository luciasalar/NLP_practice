import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
import string


def preprocess(sent):
	words = sent.split()
	new_words = []
	for w in words:
		w = w.lower()
		new_words.append(w)
	return ' '.join(new_words)



swl_data = pd.read_csv('user_all_status_swl2.csv')
swl_data_s = swl_data[:10]
s = swl_data['status']

print(s)

for x in s:
	x = str(x)
	new_x = preprocess(x)
	print(new_x)


#define tokenizer, drop everything else except for words

# def tokenize_words(x):

# 	tokenizer = RegexpTokenizer(r'\w+')
# 	token_status = x.apply(lambda row: tokenizer.tokenize(row['status']), axis=1)
# 	return token_status 

# print(tokenize_words(swl_data_s))
# words = tokenize_words(swl_data_s)

# def word_count():
# 	token_status = x.apply(lambda row: len(row['status']), axis=1)




#remove non printable string
# printable = set(string.printable)
# swl_data_s['token_status'] = filter(lambda row: row in printable, swl_data_s['token_status'])

# tagged = nltk.pos_tag(swl_data_s['token_status'])
# print(tagged)














