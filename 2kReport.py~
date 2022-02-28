import os
import sys
import numpy as np
from datetime import datetime as dt
from fpdf impoty FPDF
import matlibplot.pyplot as plt
from matplotlib import rcParams
import statistics as stat
import pandas as pd
import collectFileNames



"""
class 2kResult:
	def __init__(self, name, weight, 500Time, 1000Time, 1500Time, 2000Time):
		self.name = name
		self.weight = weight
		self.times = [500Time, 1000Time, 1500Time, 2000Time]

	def calcSplits(self):
		500Split = 500Time
		1000Split = 1000Time - 500Time
		1500Split = 1500Time - 1000Time
		2000Split = 2000Time - 1500Time
		self.splits = [500Split, 1000Split, 1500Split, 2000Split]

	def calcAverage(self)
		self.average500 = 2000Time/4

	def stdDevSplit
		self.stdDev500 = stat.stdev(splits)

	def 
"""




try:
	droppedFile = sys.argv[1]

	2kData = pd.read_json(droppedFile)
except:
	



2kData.head()


# get data

rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

def plot(data: pd.DataFrame, filename: str) -> None:
    plt.figure(figsize=(12, 4))
    plt.grid(color='#F2F2F2', alpha=1, zorder=0)
    plt.plot(data['Date'], data['ItemsSold'], color='#087E8B', lw=3, zorder=5)
    plt.title(f'Sales 2020/{data["Date"].dt.month[0]}', fontsize=17)
    plt.xlabel('Period', fontsize=13)
    plt.xticks(fontsize=9)
    plt.ylabel('Number of items sold', fontsize=13)
    plt.yticks(fontsize=9)
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()
    return

#plot 2ks by eight 
