# Opens all .txt files in a folder and
# searches for any line that matches
# a user-supplied regular expression

import re, os

textFiles = os.listdir('C:\\Users\\Melina\\AppData\\Local\\Programs\\Python\\Python36-32\\Projects\\Automate the Boring Stuff\\')

print('What do you want to search for?')
userReg = str(input())

if userReg=='email':
	stringRegex = re.compile(r'[a-z0-9]+((\.|\_)[a-z0-9]+)*@[a-z0-9]+(\.[a-z0-9]+)*(\.[a-z0-9]{2,20})')
	#fileRegex = re.compile(r'\w+\.txt')
elif userReg=='phone':
	stringRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	#fileRegex = re.compile(r'\w+\.txt')


for file in textFiles:
	openFile = open('C:\\Users\\Melina\\AppData\\Local\\Programs\\Python\\Python36-32\\Projects\\Automate the Boring Stuff\\' +file)
	readFile = openFile.readlines()
	for line in readFile:
		if stringRegex.search(line):
			print(stringRegex.search(line).group())
openFile.close()
