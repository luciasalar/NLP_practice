import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
import string
import re
#import enchant
import csv
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess(sent):

    words = str(sent).split()
    new_words = []
    new_words2 =[]
    # ps = PorterStemmer()
    
    for w in words:
        w = w.lower().replace("**bobsnewline**","").PorterStemmer()
        # remove non English word characters
        w = re.sub(r'[^\x00-\x7F]+',' ', w)
        # remove puncutation 
        w = re.sub(r'[^\w\s]','',w)
        # w = ps.stem(w)
        new_words.append(w)
        
    return ' '.join(new_words)


# def filter_non_engilsh(sent):
#   english = []
#   d = enchant.Dict("en_US")
        
#   if d.check(new_text) == True:
#       english.append(new_text)


#   return ' '.join(english)
swl_data = pd.read_csv('user_all_status_swl2.csv')

# drop column 
swl_data = swl_data.drop(swl_data.columns[[0]],axis = 1)
# print (swl_data)
swl_data = swl_data.groupby(['user_id'])
sample = swl_data['status']

strings_format = []
for i in sample:
    strings_format.append((str(i[0]), str(i[1])))

# print(type(sample))

swl_data_test['status'] = swl_data_test['status'].apply(lambda x: str(x).lower())

swl_data_test['status'] = swl_data_test['status'].apply(preprocess)

freqdsts = swl_data_test.groupby('user_id').apply((lambda x: FreqDist(str(x).split())))
freqdsts[1]

#regular expression ???
#You are working on the whole string and not on a list of tokens (this is what .split() does. Just remove it)
#Also do you want to work on the 'status' column or on everything?
clean1 = swl_data_test['status'].apply((lambda x: re.sub(r'[^\w\s]','',str(x))))


swl_data_test['status'].apply((lambda x: TextBlob(str(x))))

blobz = swl_data_test['status'].apply((lambda x: TextBlob(str(x))))   
for i in blobz:
    print(i.words)


###word cloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud().generate(str(swl_data_test['status']))


####bigram
a = nltk.bigrams(str(swl_data_test['status']).split())



####textblob

from textblob import TextBlob
swl_data_test['blobz'] = swl_data_test['status'].apply((lambda x: TextBlob(str(x))))
swl_data_test['language'] = swl_data_test['blobz'].apply((lambda x: x.detect_language()))

def english(blob):

    for i in blob:
        swl_data_test['language'] = i.detect_language()
        return swl_data_test['language']


print(english(swl_data_test['blobz']))


#difference between method and function 

 class Fooo:
     def __init__(self):
        self.Value = 0
        self.Text = "foo"
     def whatAmI(self):
        print(self.Text)
     staticFN(texttopri):
        print(texttopri)


Fooo.staticFN('dsadasdsadasdas')     #call function
a.whatAmI()     #call method






#######

# def word_count(raw_text):
#     for x in sample:
#         x = str(x)
#         new_text = preprocess(x)
#         fdist = FreqDist(new_text.split())
#         vocab = fdist.keys()
# #       swl_data_test['fdist'] = fdist
#         print(len(fdist))


# print(word_count(sample))



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

    return fdist_list

            #return fdist_list

print(freq_list(sample))

# def bigram(raw_text):
#   new_text =[]
#   for x in sample:
#       x = str(x)
#       new = preprocess(x)
#       new_text.append(new)
#       bigram_text = []
#       for i in new_text:
#           bi = nltk.bigrams(i.split())
#           bigram_text.append(bi)
#       return bigram_text

        
# print (bigram(sample))

extract_bigram_feats(document, bigrams).items()


sun_bigrams = [b for b in nltk.bigrams(cleaned_words) if (b[0] == 'sun' or b[1] == 'sun') \
  and b[0] not in stops and b[1] not in stops]


















#print(sample)


# for x in sample:
#   x = str(x)
#   new_text = preprocess(x)
#   print(new_text)






























#define tokenizer, drop everything else except for words

# def tokenize_words(x):

#   tokenizer = RegexpTokenizer(r'\w+')
#   token_status = x.apply(lambda row: tokenizer.tokenize(row['status']), axis=1)
#   return token_status 

# print(tokenize_words(swl_data_s))
# words = tokenize_words(swl_data_s)

# def word_count():
#   token_status = x.apply(lambda row: len(row['status']), axis=1)




#remove non printable string
# printable = set(string.printable)
# swl_data_s['token_status'] = filter(lambda row: row in printable, swl_data_s['token_status'])

# tagged = nltk.pos_tag(swl_data_s['token_status'])
# print(tagged)














