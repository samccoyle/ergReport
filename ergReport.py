import sys
import numpy as np
from datetime import datetime as dt
#from fpdf import FPDF
#import matplotlib.pyplot as plt
#from matplotlib import rcParams
#import statistics as stat
import pandas as pd
from raceFunc import *
from datetime import datetime, timedelta


# flags
multi_file = False
weight_data_exists = False
example = False

#Checkign if it is an example
try:
	if(sys.argv[1] == '-e'):
		os.chdir('Example')
		print('Running example')
except:
	pass
## Adding data
# get data
input_filenames = fileNames()
print('Race files read in:')
print(input_filenames)

#add data to data frame
df = pd.DataFrame()
for file in input_filenames:
	temp_df = import_df(file)
	if df.empty:
		df = temp_df
	else:
		df = pd.concat([df,temp_df],ignore_index=True)
		multi_file = True

# add weight data since it isn't in the 2k results
try:
	weightData = pd.read_excel('Weights.xlsx')
	df = pd.merge(df, weightData, how='left', on='participant')
	weight_data_exists = True
	print("Added weights")
except:
	print('Failed to add weight data, skipping')


#correcting time data units
#not using to_datetime since %m%d%y %H data is missing
temp = df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))].applymap(lambda index:datetime.strptime(index, "%M:%S.%f"))
df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))] = temp
df['time'] = df['time'].apply(lambda index:datetime.strptime(index, "%M:%S.%f"))
df['avg_pace'] = df['avg_pace'].apply(lambda index:datetime.strptime(index, "%M:%S.%f"))

## add calculations to 2k results
# standard deviation data
df['stdDev500'] = df.loc[:, df.columns.str.startswith(str('split_avg_pace_'))].std(axis=1)

#weight conversion
if weight_data_exists:

	df['conversion factor'] = df['weight'].div(270).pow(0.222)

	df['adjusted time'] = adjust_time(df['conversion factor'],df['time'])

	df['adjusted pace'] = adjust_time(df['conversion factor'],df['avg_pace'])

## Exporting data

#filtering columns for excel
filtered_df = filter_columns(df)
filtered_df = filtered_df.sort_values(by=['score'])



#saving data
with pd.ExcelWriter("results.xlsx", if_sheet_exists="replace") as writer:
	filtered_df.to_excel(writer)
print("Saved to excel")

"""
TODO add plotting and export to pdf
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

















