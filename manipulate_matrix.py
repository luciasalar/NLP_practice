import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import re
import string


dep_data = pd.read_csv('user_status_match_dep.csv')
dep = pd.read_csv('dep.csv')

#rename columns
dep_data.columns = ['drop','userid','time','status','drop2']


#merge tables
result = pd.merge(dep_data, dep, how='outer', left_on = 'userid', right_on = 'userid')

#drop and select columns
result2 = result.drop(['drop','drop2'], 1)
result2.head()

result3 = result2[['userid','time','status']].dropna()

#add frequency column
result3['freq'] = result3.groupby('userid')['userid'].transform('count')

# sort 
result4 = result3.sort_values(by=['userid','time'])

#select user status >30

result4 = result3.loc[result3['freq'] > 30]



###plot time series

result4.plot(x='time',y='freq')
plt.show()
plt.close()



#result4['new'] = result4.groupby('userid')['freq'].transform(lambda x: x*2)

###remove duplicate status in each user according to timestamp
#subset :Only consider certain columns for identifying duplicates, by default use all of the columns

dropid = result4.loc[result4.duplicated(subset=['userid', 'time']),'time'].unique()
result5 = result4[~result4.userid.isin(dropid)]


## clean data
def preprocess(sent):

    words = str(sent).split()
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

result5['status'] = result5['status'].apply(lambda x: preprocess(x))


# remove non-English 
en_words = set(nltk.corpus.words.words())

def remove_eng(sent, en_words):

    words = str(sent).split()
   
    new_words = []

    for w in words:
        if w.lower in en_words:
            new_words.append(w)
    return ' '.join(new_words)



result5['status'] = result5['status'].apply(lambda x: remove_eng(x))



df['sentiment'] = df['status'].apply(lambda x: TextBlob(x))


def find_close_w(sent):

    words = str(sent).split()
   
    new_words = []

    for w in words:
        s = edit_distance(w, "shine")
        new_words.append(s)
    return new_words

df['status'].apply(lambda x: find_close_w(x))




