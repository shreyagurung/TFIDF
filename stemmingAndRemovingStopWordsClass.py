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
ceestr=""
cst=""
wnl = WordNetLemmatizer()
chocolateStr=(" ".join([wnl.lemmatize(i) for i in chocolateStr.split()]))
coffeeStr=(" ".join([wnl.lemmatize(j) for j in coffeeStr.split()]))
cheeseStr=(" ".join([wnl.lemmatize(k) for k in cheeseStr.split()]))
list3=[]
global list1
list1=[]
list3=[cheeseStr,chocolateStr,coffeeStr]
for item in list3:
	words = item.split()
	for r in words:    	
		if not r in stop_words: 
			ceestr=ceestr+" "+r
	list1.append(ceestr)
	ceestr=" "



	
