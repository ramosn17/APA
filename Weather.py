#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 02:33:54 2020

@author: user
"""

import operator
from os import listdir
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import *
from numpy import linalg as la
import numpy as np
import scipy.linalg as SL
import numpy
import statsmodels.formula.api as smf
import datetime as dt
from scipy.stats.stats import pearsonr
import statsmodels.api as sm
from scipy import stats

import csv

print("Weather Dataset")

#%%Read the CSV file to a Dataframe entitled Weather


weather = pd.read_csv("weather.csv")

#%% Review columns, first five rows and dataframe information
print(weather.columns)
print(weather.head(5))
print(weather.info())

#%% Split the 'Date' key utilizing the  module 'datetime' into a format Pandas can accept. 
##The 'Date' key wil be split into 'Months' and 'Year' columns', the later of which will be utilized to m
#merge the datafiles. 

weather['Datetime'] = pd.to_datetime(weather.Date, format='%Y/%m/%d')
weather['Date'] = weather['Datetime'].apply(lambda x:x.date())
weather['Month'] = weather['Datetime'].apply(lambda x:x.month)
weather['Year'] = weather['Datetime'].apply(lambda x:x.year)

print(weather.Year)

#%%The  groupby function will enable us to split the data into  
   #groups based on the 'Year' key, apply the 'group' function to each element  
  # and combine the results into a dataframe ('grouped_weather'). Make sure to 
  #reset the index, or the 'Year' key will not be included. 


grouped_weather = weather.groupby(['Year']).mean().reset_index()


#%%Add keys to the dataframe

grouped_weather = grouped_weather[['Year', 'Max TemperatureF', 'Mean TemperatureF',
       'Min TemperatureF','Max Humidity', ' Mean Humidity', ' Min Humidity',
       'PrecipitationIn']]

grouped_weather.head()

print(grouped_weather.info())
print(grouped_weather.columns)

#%% Copy to a .csv file for merging later 
grouped_weather.to_csv("grouped_weather.csv", index = False, header = True, sep = ',', encoding = 'utf-8')








