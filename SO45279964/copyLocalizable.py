#!/usr/bin/python

import sys

supportedLanguages = ["en","pl"]
commonPath = ".lproj/Localizable.strings"
keys = ["AppName"]

class CopyLocalizable():
	
	target = ""

	def __init__(self,arg):
		self.target = arg
		self.perform()
	
	def perform(self):
		for lang in supportedLanguages:
			pathToLocalizable = lang+commonPath
			textToFile = ""
			with open(pathToLocalizable,"r") as languageFile:		   
				for line in languageFile.readlines():
					for key in keys:
						if key in line:
							textToFile += self.foundAndReplace(key,lang)
						else:
							textToFile += line
			self.saveInFile(pathToLocalizable,textToFile)
		

	def foundAndReplace(self,key,lang):
		pathToTargetFile = "Localizable/"+lang+".lproj/"+self.target+".strings"
		with open(pathToTargetFile,"r") as targetFile:
			for targetLine in targetFile.readlines():
				if key in targetLine:
					return targetLine
					
	def saveInFile(self,file,stringToSave):
		with open(file,"w+") as languageFile:
			languageFile.write(stringToSave)