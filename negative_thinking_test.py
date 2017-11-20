import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import re
import string


neg_data = pd.read_csv('negative_thinking_test.csv')
dep = pd.read_csv('dep.csv')


#merge tables
#result = pd.merge(neg_data, dep, how='outer', left_on = 'userid', right_on = 'userid')

#assign  'Neutral = 0' to level 1 and level3 
# NT= 1, R = 1, W = 2

#recode
def recode_NT(series):
    if series == 'NT':
        return 1
    elif series != 'NT':
        return 0


  
def recode_L3(series):
    if series == 'R':
        return 1
    elif series == 'W':
        return 2
    elif series == '0':
        return 0

#make a new copy
neg_data2  = neg_data[:]      

neg_data2['level_1'] = neg_data2['level_1']. apply(recode_NT)

neg_data2['level_3'] = neg_data2['level_3']. apply(recode_L3)


#drop and select columns
#result2 = result[['userid','time','status','level_1','level_3']].dropna()

# sort 
neg_data2 = neg_data2.sort_values(by=['userid','time'])

#add frequency column
neg_data2['freq'] = neg_data2.groupby('userid')['userid'].transform('count')

#select user status >30
#result4 = result3.loc[result3['freq'] > 30]



###plot time series

neg_data2.plot(x='time',y='freq')
plt.show()
plt.close()


###remove duplicate status in each user according to timestamp
#subset :Only consider certain columns for identifying duplicates, by default use all of the columns

dropid = neg_data2.loc[neg_data2.duplicated(subset=['userid', 'time']),'time'].unique()
neg_data2= neg_data2[~neg_data2.userid.isin(dropid)]

neg_data3 = neg_data2[:]

## clean data
def preprocess(sent):

    words = str(sent).split()
    new_words = []
  
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

neg_data3['status'] = neg_data3['status'].apply(lambda x: preprocess(x))


# remove non-English 
en_words = set(nltk.corpus.words.words())

def remove_eng(sent, en_words):

    words = str(sent).split()
   
    new_words = []

    for w in words:
        if w.lower in en_words:
            new_words.append(w)
    return ' '.join(new_words)


neg_data3['status'] = neg_data3['status'].apply(lambda x: remove_eng(x, en_words