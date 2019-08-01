import os, glob
import os
import io
class coffee:
	os.chdir('G:\TFIDF\documents\coffee')
	files = glob.glob("*.txt")
	global list_coffee
	list_coffee=[]
	global coffeeStr
	for file1 in files:
		with open (file1, 'r') as myfile:
			data=myfile.read().replace("\n","")
		list_coffee.append(data)
	
		coffeeStr=str(list_coffee)
	
