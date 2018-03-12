import math
from textblob import TextBlob as tb
import os
import io
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from stemmingAndRemovingStopWordsFullDocument import list2
from stemmingAndRemovingStopWordsClass import list1
from cheese import list_cheese
from chocolate import list_chocolate
from coffee import list_coffee
from collections import Counter
os.chdir('G:\TFIDF')

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_doc(word, lists):
    return sum(1 for blob in lists if word in lists)

def idf(word, lists):
    return math.log(len(lists) / (1 + n_doc(word, lists)))

def tfidf(word, blob, lists):
    return tf(word, blob) * idf(word,lists)
bloblist=[]
blobclass=[]
list_word=[]
finalist=[]
finalist1=[]
for item in list1:
    blobclass.append(tb(item))
    #print(item)
for item in list2:
    bloblist.append(tb(item))
    #print(item)
print("TFIDF for documents in a class")
for i, blob in enumerate(blobclass):
    #print("Top word in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, blobclass) for word in blob.words}
    #print(scores)
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words:
        finalist1.append("%s:%s"%(word, round(score, 5)))
        #print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
print("TFIDF for the whole set of documents")
for i, blob in enumerate(bloblist):
    #print("Top word in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    #print(scores)
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words:
        finalist.append("%s:%s "%(word,round(score,5)))
        #print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
        list_word.append(word)
thefile=open('TFID.txt','w')
for item in finalist:
  thefile.write("%s\n" % item)
thefile1=open('TFID1.txt','w')
for item in finalist1:
  thefile1.write("%s\n" % item)
        
#print(list_word)


