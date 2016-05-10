#!/usr/bin/python

import random
import sys
import os

def transformInputIntoRisk(input):
	riskNum = random.randint(1,20)
	riskNum = int(riskNum/2 + 0.5)
	return(riskNum)

def convertRiskNumberToRiskLevel(riskNum):
	if(riskNum == 0):
		return('Informational')
	elif(riskNum > 0 and riskNum < 4):
		return('Low')
	elif(riskNum >= 4 and riskNum < 7):
		return('Medium')
	elif(riskNum >= 7 and riskNum < 10):
		return('High')
	elif(riskNum == 10):
		return('Uber Critical')
	else:
		return('How did you even get this score?')


def getSuperImportantUserInput():
	pyVersion = sys.version[0]
	if(int(pyVersion) < 3):
		superImportant = raw_input()
	else:
		superImportant = input()
	return(superImportant)

	
def clearScreen():
	if(sys.platform[:3]=='win'):
		os.system("cls")
	else:
		os.system("clear")
	
while(True):
	clearScreen()
	print('[*] Please input all data on the vulnerability, followed by a single newline. This can be anything \(name, description, impact, likelyhood, etc\): ')
	riskNum = transformInputIntoRisk(getSuperImportantUserInput())
	riskLevel = convertRiskNumberToRiskLevel(riskNum)
	print('[*] That vulnerability is classified as...')
	print('[*] Risk Score: ' + str(riskNum))
	print('[*] Risk Level: ' + riskLevel)
	print('\nPress enter to input a new vulnerability')
	getSuperImportantUserInput()