import os
import sys

def names():
	#	find all files ending in a certain extension
	files = []
	for file in os.listdir(folder):
		if file.endswith('.JSON'):
		files += file
	return files

def squads():
 #return: men, women, novice varsity 
	return 0 