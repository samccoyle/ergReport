import os
import sys
import numpy as np
from datetime import datetime as dt
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib import rcParams
import statistics as stat
import pandas as pd
from raceFunc import *
from datetime import datetime

# flags
multi_file = False
weight_data = False

# get data
input_filenames = fileNames()

#add data to data frame
df = pd.DataFrame()
for file in input_filenames:
	temp_df = import_df(file)
	if df.empty:
		df = temp_df
	else:
		df = pd.concat([df,temp_df],ignore_index=True)
		print('Added {0}',file)
		multi_file = True

# add weight data since it isn't in the 2k results 
try:
	weightData = pd.read_excel('Weights.xlsx')
	df.merge(weightData, how='left', left_on='participant', right_on='Name')
except:
	print('Failed to add weight data, skipping')
	weight_data = True

#correcting time data
#not using to_datetime since %m%d%y %H data is missing
df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))] = time_convert(
	df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))])

df['time'] = time_convert(df['time'])

# add calculations to 2k results

# standard deviation data 
df['stdDev500'] = df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))].std(axis=1)
print(df.head(20))

#weight conversion




# saving data
df.to_excel('results.xlsx')



with pd.ExcelWriter("results.xlsx", if_sheet_exists="replace") as writer:
	df.to_excel(writer)


"""
plot 2ks by eight
2kData.sort_values([''])
athleteCount= = len(2kData.index)
currentIndex = 0
for ii in range(athleteCount):
	plotData = 2kData.iloc[currentIndex:(currentIndex+8)]
	filename = dataFilename + " " + currentIndex "-" + (currentIndex + 7)
	plot(plotData,filename)
	currentIndex += 8
"""

















