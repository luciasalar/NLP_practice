# Simple translation model and language model data structures
import sys
from collections import namedtuple

# A translation model is a dictionary where keys are tuples of French words
# and values are lists of (english, logprob) named tuples. For instance,
# the French phrase "que se est" has two translations, represented like so:
# tm[('que', 'se', 'est')] = [
#   phrase(english='what has', logprob=-0.301030009985), 
#   phrase(english='what has been', logprob=-0.301030009985)]
# k is a pruning parameter: only the top k translations are kept for each f.
phrase = namedtuple("phrase", "english, logprob")
def TM(filename, k):
  sys.stderr.write("Reading translation model from %s...\n" % (filename,))
  tm = {}
  for line in open(filename).readlines():
    (f, e, logprob) = line.strip().split(" ||| ")
    tm.setdefault(tuple(f.split()), []).append(phrase(e, float(logprob)))
  for f in tm: # prune all but top k translations
    tm[f].sort(key=lambda x: -x.logprob)
    del tm[f][k:] 
  return tm

# # A language model scores sequences of English words, and must account
# # for both beginning and end of each sequence. Example API usage:
# lm = models.LM(filename)
# sentence = "This is a test ."
# lm_state = lm.begin() # initial state is always <s>
# logprob = 0.0
# for word in sentence.split():
#   (lm_state, word_logprob) = lm.score(lm_state, word)
#   logprob += word_logprob
# logprob += lm.end(lm_state) # transition to </s>, can also use lm.score(lm_state, "</s>")[1]
ngram_stats = namedtuple("ngram_stats", "logprob, backoff")
class LM:
  def __init__(self, filename):
    sys.stderr.write("Reading language model from %s...\n" % (filename,))
    self.table = {}
    for line in open(filename):
      entry = line.strip().split("\t")
      if len(entry) > 1 and entry[0] != "ngram":
        (logprob, ngram, backoff) = (float(entry[0]), tuple(entry[1].split()), float(entry[2] if len(entry)==3 else 0.0))
        self.table[ngram] = ngram_stats(logprob, backoff)

  def begin(self):
    return ("<s>",)

  def score(self, state, word):
    ngram = state + (word,)
    score = 0.0
    while len(ngram)> 0:
      if ngram in self.table:
        return (ngram[-2:], score + self.table[ngram].logprob)
      else: #backoff
        score += self.table[ngram[:-1]].backoff if len(ngram) > 1 else 0.0 
        ngram = ngram[1:]
    return ((), score + self.table[("<unk>",)].logprob)
    
  def end(self, state):
    return self.score(state, "</s>")[1]
  
  def fullScore(self, sentence):
      lm_state = self.begin() # initial state is always <s>
      logprob = 0.0
      for word in sentence.split():
          (lm_state, word_logprob) = self.score(lm_state, word)
          logprob += word_logprob
      logprob += self.end(lm_state) # transition to </s>, can also use
      return logprob


import nltk
import sys

# Import the Presidential inaugural speeches corpus
from nltk.corpus import inaugural

# Import the gutenberg corpus                                                                               
from nltk.corpus import gutenberg


# Import NLTK's NgramModel module (for building language models)
# It has been removed from standard NLTK, so we access it in a special package installation
sys.path.extend(['/group/ltg/projects/fnlp', '/group/ltg/projects/fnlp/packages_2.6'])
from nltk import NgramModel
from nltk import compat

#################### EXERCISE 1 ####################

# Solution for exercise 1
# Input: doc_name (string)
# Output: total_words (int), total_distinct_words (int)
def ex1(doc_name):    # Use the plaintext corpus reader to access a pre-tokenised list of words
    # for the document specified in "doc_name"
    doc_words = inaugural.words(doc_name)

    # Find the total number of words in the speech
    total_words = len(doc_words)

    # Find the total number of DISTINCT words in the speech
    total_distinct_words = len(set(doc_words))

    # Return the word counts
    return (total_words, total_distinct_words)


### Uncomment to test exercise 1
speech_name = '2009-Obama.txt'
(tokens,types) = ex1(speech_name)
print ("Total words in %s: %s"%(speech_name,tokens))
print ("Total distinct words in %s: %s"%(speech_name,types))



#################### EXERCISE 2 ####################

# Solution for exercise 2
# Input: doc_name (string)
# Output: avg_word_length (float)
def ex2(doc_name):
    doc_words = inaugural.words(doc_name)

    # Construct a list that contains the word lengths for each DISTINCT word in the document
    list =[]
    for i in doc_words:
        list.append(len(set(i)))

    distinct_word_lengths = list

    # Find the average word length
    avg_word_length = sum(list)/len(set(doc_words))

    # Return the average word length of the document
    return avg_word_length


### Uncomment to test exercise 2 
speech_name = '2009-Obama.txt'
result2 = ex2(speech_name)
print ("Average word length for %s: %s"%(speech_name,result2))



#################### EXERCISE 3 ####################

# Solution for exercise 3
# Input: doc_name (string), x (int)
# Output: top_words (list)
def ex3(doc_name, x):
    doc_words = inaugural.words(doc_name)
    
    # Construct a frequency distribution over the lowercased words in the document
    fd_doc_words = nltk.FreqDist(w.lower() for w in doc_words)

    # Find the top x most frequently used words in the document
    #top_words =  filter(lambda x:fd_doc_words[x] > 3,fd_doc_words.values())
    top_words = fd_doc_words.most_common(50)
    # Return the top x most frequently used words
    return top_words


### Uncomment to test exercise 3
#print "Top 50 words for Obama's 2009 speech:"
result3a = ex3('2009-Obama.txt', 50)
print (result3a)
#print "Top 50 words for Washington's 1789 speech:"
result3b = ex3('1789-Washington.txt', 50)
print (result3b)



#################### EXERCISE 4 ####################

# Solution for exercise 4
# Input: doc_name (string), n (int)
# Output: lm (NgramModel language model)
def ex4(doc_name, n):
    # Construct a list of lowercase words from the document
    words = [w.lower() for w in gutenberg.words(doc_name)]

    # Build the language model using the nltk.MLEProbDist estimator 
    est = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
    lm = NgramModel(3,words,estimator=est)
    
    # Return the language model (we'll use it in exercise 5)
    return lm


### Uncomment to test exercise 4
result4 = ex4('austen-sense.txt',2)
#print "Sense and Sensibility bigram language model built"



#################### EXERCISE 5 ####################

# Solution for exercise 5
# Input: lm (NgramModel language model, from exercise 4), word (string), context (list)
# Output: p (float)
def ex5(lm,word,context):
    # Compute the probability for the word given the context
    #p = 

    # Return the probability
    return p


### Uncomment to test exercise 5
#result5a = ex5(result4,'for',['reason'])
#print "Probability of \'reason\' followed by \'for\': %s"%result5a
#result5b = ex5(result4,'end',['the'])
#print "Probability of \'the\' followed by \'end\': %s"%result5b
#result5c = ex5(result4,'the',['end'])
#print "Probability of \'end\' followed by \'the\': %s"%result5c

### Uncomment to test exercise 6
#result6 = ex5(result4,'the',['end'],True)
