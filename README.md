# TF*IDF or Term Frequency * Inverse Document Frequency
TF\*IDF is a technique to retrieve information from a vast space. For example when you type a word on Google how does Google know which are the relevant articles to show from the n number of articles published. Google had been using TF\*IDF to get the relevance of an important keyword in an article thereby concluding what the article is about.TF\*IDF calculates the importance and relevance of keywords.
The project done is a very small example of TF\*IDF using data that I made on my own just for experimental purposes to get an understanding of TF/*IDF
## Installation
This project is done in the language PYTHON <br>
Packages required: nltk and textblob <br>
Visit the [nltk site](https://www.nltk.org/) to download the nltk package <br>
Visit the [textblob site](https://pypi.org/project/textblob/) to download the textblob package <br>
## Formula
TF: Term Frequency, which measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often divided by the document length (aka. the total number of terms in the document) as a way of normalization: 

**TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).**

IDF: Inverse Document Frequency, which measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scale up the rare ones, by computing the following: 

**IDF(t) = log_e(Total number of documents / Number of documents with term t in it).**

## Explanation of Code
The [function.py](https://github.com/shreyagurung/TFIDF/blob/master/function.py) calculates the TF*IDF. Here the helper functions are called like [stemmingAndRemovingStopWordsClass.py](), this function removes and stems StopWords (commonly used words such as 'a','the','that,'an','in', etc). NLTK has an inbuilt function to remove it directly.
There are three other classes that are imported namely the 3 dangerous Cs Coffee, Chocolate and Cheese. These classes extract words from a document and store them in lists.


