from nltk.stem import PorterStemmer, WordNetLemmatizer
from chocolate import list_chocolate,chocolateStr
from coffee import list_coffee,coffeeStr
from cheese import list_cheese,cheeseStr
import os
import io
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
os.chdir('G:\TFIDF')
stop_words = set(stopwords.words('english'))
global string1
global list3
list3=[]
list1=[]
ceestr=""
cst=""
wnl = WordNetLemmatizer()
for item in list_cheese:
	cheeseStr=(" ".join([wnl.lemmatize(i) for i in item.split()]))
	cst=cheeseStr+" "+cheeseStr
	list1.append(cheeseStr)
for item in list_chocolate:
	chocolateStr=(" ".join([wnl.lemmatize(i) for i in item.split()]))
	list1.append(chocolateStr)
for item in list_coffee:
	coffeeStr=(" ".join([wnl.lemmatize(j) for j in item.split()]))
	list1.append(coffeeStr)
global list2
list2=[]	
for item in list1:
	words = item.split()
	for r in words:    	
		if not r in stop_words: 
			ceestr=ceestr+" "+r
	list2.append(ceestr)
	ceestr=" "
	
	

	
