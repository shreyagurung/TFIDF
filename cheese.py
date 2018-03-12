import os, glob
import os
import io
class cheese:
	os.chdir('G:\TFIDF\documents\cheese')
	files = glob.glob("*.txt")
	global list_cheese
	list_cheese=[]
	global cheeseStr
	for file1 in files:
		with open (file1, 'r') as myfile:
			data=myfile.read().replace("\n","")
		list_cheese.append(data)
	#for item in list_cheese:
	#	print(item)
	
		cheeseStr=str(list_cheese)

  	#for item in list_cheese:
	#	for plural in item.split():
	#		list_cheese2.append(stemmer.stem(plural))
	#	cheeseStr=' '.join(list_cheese2)
	#print(cheeseStr)
	#for item in list_cheese2:
	#	print(item)
	#cheeseStr=str(list_cheese2)