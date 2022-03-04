import sys
import numpy as np
from datetime import datetime as dt
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib import rcParams
import statistics as stat
import pandas as pd
from raceFunc import *
from datetime import datetime, timedelta

#constansts
cox_weight = 130
boat_weight_8 = 200
boat_weight_4 = 125

# flags
multi_file = False
weight_data_exists = False

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
		#print('Added {0}',file)
		multi_file = True

# add weight data since it isn't in the 2k results
try:
	weightData = pd.read_excel('Weights.xlsx')
	df = pd.merge(df, weightData, how='left', on='participant')
	weight_data_exists = True
	df['boat weight 4'] = df['weight'] + cox_weight/4 + boat_weight_4/4
	df['boat weight 8'] = df['weight'] + cox_weight/8 + boat_weight_8/8
	print("Added weights")
except:
	print('Failed to add weight data, skipping')


#correcting time data
#not using to_datetime since %m%d%y %H data is missing
temp = df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))].applymap(lambda index:datetime.strptime(index, "%M:%S.%f"))
df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))] = temp
df['time'] = df['time'].apply(lambda index:datetime.strptime(index, "%M:%S.%f"))
df['avg_pace'] = df['avg_pace'].apply(lambda index:datetime.strptime(index, "%M:%S.%f"))

# add calculations to 2k results

# standard deviation data 
df['stdDev500'] = df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))].std(axis=1)

#weight conversion
if weight_data_exists:

	df['conversion factor'] = df['weight'].div(270).pow(0.222)
	df['conversion factor 4']= df['boat weight 4'].div(270).pow(0.222)
	df['conversion factor 8']= df['boat weight 8'].div(270).pow(0.222)

	df['adjusted score'] = adjust_time(df['conversion factor'],df['time'])
	df['4 score'] = adjust_time(df['conversion factor 4'],df['time'])
	df['8 score'] = adjust_time(df['conversion factor 8'],df['time'])

	df['adjusted pace'] = adjust_time(df['conversion factor'],df['avg_pace'])
	df['4 pace'] = adjust_time(df['conversion factor 4'],df['avg_pace'])
	df['8 pace'] = adjust_time(df['conversion factor 8'],df['avg_pace'])

# filtering data for saving
string_to_filter = ['id, 
	'calories',
	'class',
	'lane',
	'log',
	'machine',
	'serial',
	'running']
temp2 = df.columns.str.startswith(str('split_avg_pace_'))
temp3 = temp2.copy()
temp2[1] = True
temp3[2] = True
temp4 = temp2 + temp3
print(temp2)
print(temp3)
print(temp4)

#saving data
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

















