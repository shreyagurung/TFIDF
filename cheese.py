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
	
		cheeseStr=str(list_cheese)
