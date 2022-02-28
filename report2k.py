import os
import sys
import numpy as np
from datetime import datetime as dt
from fpdf impoty FPDF
import matlibplot.pyplot as plt
from matplotlib import rcParams
import statistics as stat
import pandas as pd
import 2kHelper as 2k


# get data
columnHeaders = []
2kData = pd.DataFrame(columnHeaders)
dataFilename = ""

try:
	droppedFile = sys.argv[1]
	2kData.append(pd.read_json(droppedFile))
	dataFilename = droppedFile
except:
	files = collectFiles.names()
	for name in files:
		tempData = pd.read_json(name)
		tempColumnHeaders = 2kData.columns.values
		if list(tempColumnHeaders) == columnHeaders:
			2kData.append(tempData)
		else:
			print("Skipping {0}, incorrect filetype", name)
	dataFIlename = "2k Results"

# slicing data to remove unnecessary 
sliceParticipants(2kData)



# add weight data since it isn't in the 2k results 

try:
	weightData = pd.read_excel('weights.xlsx')
	2kData.merge(weightData[['Weight', 'Name']], how = 'left')
except:
	raise Exception("Missing weight data")




#2kData.head()

2k.weights

# plot manipulation
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

def plot(data: pd.DataFrame, filename: str) -> None:
	plt.figure(figsize=(12, 4))
	plt.grid(color='#F2F2F2', alpha=1, zorder=0)
	plt.plot(data['Name'], data['500'],data['1000'],data['1500'],data['2000'], color='#087E8B', lw=3, zorder=5)
	plt.title(f'2k Pace', fontsize=17)
	plt.xlabel('Distance [m]', fontsize=13)
	plt.xticks(fontsize=9)
	plt.ylabel('Pace [sec/500m]', fontsize=13)
	plt.yticks(fontsize=9)
	plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
	plt.close()
	return

#plot 2ks by eight 
2kData.sort_values([''])
athleteCount= = len(2kData.index)
currentIndex = 0
for ii in range(athleteCount):
	plotData = 2kData.iloc[currentIndex:(currentIndex+8)]
	filename = dataFilename + " " + currentIndex "-" + (currentIndex + 7)
	plot(plotData,filename)
	currentIndex += 8


















