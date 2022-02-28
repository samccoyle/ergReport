import os
import sys
import numpy as np
from datetime import datetime as dt
#from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib import rcParams
import statistics as stat
import pandas as pd
import raceFunc as rf
import json

# get data
#columnHeaders = []
#data = pd.DataFrame(columnHeaders)
dataFilename = "Event 2 - Novice Men 2k.json"

f = open(dataFilename)
data_import = json.load(f)

#print(data_import)

data = pd.json_normalize(
	data_import,
	record_path=['results' , 'participants'])
	#meta=['results', 'participants' ,'splits'])

print(data.head(20))

#print

flat_df = []
splits_col = data['splits']

print(splits_col)
for splits in splits_col:
#	print(splits)
	temp_dic = {}
	for split in splits:
		running_dist = str(split['split_running_distance'])
		for key in split:
			new_key  = key + '_' + running_dist
			temp_dic[new_key] = split[key]
	flat_df.append(temp_dic)


expanded_df = pd.DataFrame(flat_df)

names = data['participant']
expanded_df.insert(0, 'participant', list(names))
print(expanded_df.head(20))
del data['splits']
final_df = data.merge(expanded_df, how='left')
print(data.head(16))
final_df.to_excel('results.xlsx')


"""
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
    dataFilename = "2k Results"
"""
