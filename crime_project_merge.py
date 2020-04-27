#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:11:13 2020

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
import plotly.graph_objs as go
import plotly.express as px

df_final = pd.read_csv('df.csv')
weather = pd.read_csv('grouped_weather.csv')
unemployment = pd.read_csv('unemployment3.csv')
#%% 
print(unemployment.info())
print(weather.info())
print(df_final.info())


#%%Create a variable named 'analysis_dataset' and set it equal to the pd.merge function. Within this function, we will merge  
   #df_final and weather on the 'Year' key. 

analysis_dataset = pd.merge(df_final, weather,on=['Year'])
analysis_dataset = pd.merge(analysis_dataset,unemployment, on=['Year'])

#%%Print "Analysis Dataset Information" and then print the first five rows of the dataframe. 
print("Analysis Dataset Information")
print(analysis_dataset.head(5))

#%% Copy the merged dataframe to a .csv file
analysis_dataset.to_csv("crime_info2.csv")

print(analysis_dataset.columns)
print(analysis_dataset.info())


#%% Excercise the groupby()funciton to explore the data pertaining to Primary Crime
#type and Mean Temperature by year. The keys will be indexed by 'counts' for primary
#crime types, sorted and exported to a .csv file. 



group_final = analysis_dataset.groupby(["Month", "Primary Type","Year", "Mean TemperatureF", "Max TemperatureF"]).size().reset_index(name = 'counts')  
group_final = group_final.sort_values(["Month","Primary Type","Year", "Mean TemperatureF", "Max TemperatureF"], ascending = False, inplace=False, kind= 'quicksort', na_position= 'last')

print(group_final)

group_final.reset_index().to_csv("weather_crime.csv", index = False, header = True, sep = ',', encoding = 'utf-8')


#%% Similiar to the previous command, this groupby() will enable us to explore any similiarities in Primary
#Crime type and unemployment rate by year. This data is similiarly grouped, sorted and exported to a .csv file. 
group_final2 = analysis_dataset.groupby([ "Year", "Primary Type", "unemployment rate"]).size().reset_index(name = 'counts')  
group_final2 = group_final2.sort_values(["Primary Type", "unemployment rate", "Year"])

group_final2.to_csv("unemprate.csv", index = False, header = True, sep = ',', encoding = 'utf-8')
#%%

group_final3 = analysis_dataset.groupby(["Mean TemperatureF", "Primary Type"]).size()
print(group_final3)

group_final3.reset_index().to_csv("group_final3.csv", index = False, header = True, sep = ',', encoding = 'utf-8')