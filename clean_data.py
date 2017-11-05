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

# drop column 
swl_data = swl_data.drop(swl_data.columns[[0]],axis = 1)
# print (swl_data)
swl_data = swl_data.groupby(['user_id'])
sample = swl_data['status']
# print(type(sample))

def word_count(raw_text):
	for x in sample:
		x = str(x)
		new_text = preprocess(x)
		fdist = FreqDist(new_text.split())
		vocab = fdist.keys()
		print(fdist["he"])

#print(word_count(sample))



# count modal verbs

def modal_count(raw_text):
	new_text =[]
	for x in raw_text:
		x = str(x)
		new = preprocess(x)
		new_text.append(new)
		fdist = FreqDist(new_text.split())
		modals = ['can']
		for m in modals:
			print (m + ':', fdist[m])

#print(modal_count(sample))


def freq_list(raw_text):
	new_text =[]
	for x in raw_text:
		x = str(x)
		new = preprocess(x)
		new_text.append(new)
		fdist_list = []
		for i in new_text:
			fdist = FreqDist(i.split())
			fdist_list.append(fdist)
			print (fdist_list)

			#return fdist_list

print(freq_list(sample))

#print(sample)


# for x in sample:
# 	x = str(x)
# 	new_text = preprocess(x)
# 	print(new_text)






























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














