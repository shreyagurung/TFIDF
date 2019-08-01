import os, glob
class chocolate:
	os.chdir('G:\TFIDF\documents\chocolate')
	files = glob.glob("*.txt")
	global list_chocolate
	list_chocolate=[]
	global chocolateStr
	for file1 in files:
		with open (file1, 'r') as myfile:
			data=myfile.read().replace("\n","")
		list_chocolate.append(data)
	
		chocolateStr=str(list_chocolate)
	
