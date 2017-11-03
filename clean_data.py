import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
import string
import re
import enchant

def preprocess(sent):

	words = sent.split()
	new_words = []
	new_words2 =[]
	# ps = PorterStemmer()
	
	for w in words:
		w = w.lower().replace("**bobsnewline**","")
		# remove non English word characters
		w = re.sub(r'[^\x00-\x7F]+',' ', w)
		# remove puncutation 
		w = re.sub(r'[^\w\s]','',w)
		# w = ps.stem(w)
		new_words.append(w)
		
	return ' '.join(new_words)


# def filter_non_engilsh(sent):
# 	english = []
# 	d = enchant.Dict("en_US")
		
# 	if d.check(new_text) == True:
#  		english.append(new_text)


# 	return ' '.join(english)
swl_data = pd.read_csv('user_all_status_swl2.csv')

# swl_data_s = swl_data[:10]
swl_data = swl_data.drop(swl_data.columns[[0]],axis = 1)
# print (swl_data)
swl_data = swl_data.groupby(['user_id'])
sample = swl_data['status']

for x in sample:
	# x = str(x)
	new_text = preprocess(x)
	# print(new_text)


for i in sample:
	print (i)

# def frequency(text):
# 	for i in text:
# 		fdist = FreqDist(i)

# 		# vocab = fdist.keys()
# 	return fdist




# print(frequency(new_text))























# print (filter_non_engilsh(new_text))

# word frequency
# def word_frequency (count,total):
# 	return 100* count/total


# print(word_frequency(new_text.count("he"),len(new_text)))

# frequency distribution























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














