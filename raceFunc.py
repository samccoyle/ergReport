
def fileNames():
	#	find all files ending in a certain extension
	files = []
	for file in os.listdir(folder):
		if file.endswith('.JSON'):
			files += file
	return files

def squads():
 #return: men, women, novice varsity 
	return 0 

def weightImport(names):
	try:
		weightData = pd.read_excel('weights.xlsx')
	except:
		raise Exception("Missing weight data")
	weightData.sort_values(by=['Name'])
	#check names
	for index, row in weightData.iterrows():
		print("Hello")



