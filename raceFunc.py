
import numpy as np
import os
import sys
import pandas as pd
import glob
from pathlib import Path
import json
from datetime import datetime, timedelta

def fileNames():
	files = []
	#	find all files ending in a certain extension
	folder = Path().absolute()
	for file in glob.glob("*.json"):
		files.append(file)
	for file in glob.glob("*.JSON"):
		files.append(file)
	return files

def expand_splits(splits_col):
	flat_dicts = []
	for splits in splits_col: #iterating through each row of the column
	    temp_dic = {}
	    for split in splits: #iterating thorugh each split segment
	        running_dist = str(split['split_running_distance'])
	        for key in split: # changing the keys to match the current completed distance for future expansion
	            new_key  = key + '_' + running_dist
	            temp_dic[new_key] = split[key]
	    flat_dicts.append(temp_dic)
	return flat_dicts

def import_df(filename):
	#create a data frame from a file
	f = open(filename)
	data_import = json.load(f)
	data = pd.json_normalize(
	    data_import,
	    record_path=['results' , 'participants'])

	#expanding the list of dicts in the splits column
	flat_splits = expand_splits(data['splits'])
	expanded_df = pd.DataFrame(flat_splits)

	#merging the expanded data into the previous data
	names = data['participant']
	names.columns = ['participant']
	expanded_df.insert(0, 'participant', names)
	del data['splits']
	final_df = data.merge(expanded_df, how='left' , left_on=['participant'], right_on=['participant'])
	return final_df

def time_convert(time_data):
	datetime_data = time_data.applymap(lambda index:datetime.strptime(index, "%M:%S.%f"))
	return datetime_data

def adjust_time(conversion_factor,duration):
	df = pd.concat([conversion_factor, duration], join='outer', axis=1)
	adjusted_times = []
	for factor, time in df.itertuples(index=False):
		try:
			adjusted_time = time + timedelta(seconds=timedelta(minutes=time.minute, seconds=time.second, microseconds=time.microsecond).total_seconds() * (factor - 1))
		except:
			adjusted_time = time
		adjusted_times.append(adjusted_time)

	converted_times = pd.DataFrame(adjusted_times, columns=['adjusted timestamps'])
	converted_times['adjusted times'] = pd.to_datetime(converted_times['adjusted timestamps'])
	return converted_times['adjusted times']

def column_name_mask(text, df):
	try:
		temp = df.columns.str.contains(str(text))

	except:
		temp = df.columns.str.startswith(str(text))
		print('failed')
	return temp

def filter_columns(df):
	# reading in columsn to ignore
	try:
		with open('columns_ignore.txt') as f:
		    string_to_filter = [line.strip('\n') for line in f]
		print('Read in filtered columns')
	except:
		print('Failed to read in filtered columns, no filter applied')
		return df

	mask = []
	for text in string_to_filter:
	    mask_text = column_name_mask(text,df)
	    if len(mask) > 0:
	        mask = mask + mask_text
	    else:
	        mask = mask_text

	mask = np.logical_not(mask)

	final_df = df.loc[:, mask]
	return final_df


def squads():
 #return: men, women, novice varsity
	return 0



