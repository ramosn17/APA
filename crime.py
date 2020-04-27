#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:44:02 2020

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
import seaborn as sns
from sklearn.ensemble import AdaBoostClassifier
from sklearn.utils import shuffle

import plotly.graph_objs as go
import plotly.express as px
import calendar

#%% Import the datafile as crime_data

crime_data = pd.read_csv("Crimes_-_2001_to_present.csv", low_memory= False)

#%%Review the columns in the datafile by attaching the .columns attribute to the end    of  
    #the variable 'crime_data.' Print this attribute and label the action "Crime  
    #Dataset Columns."
#%%Integrate the .info attribute to the end of 'crime_data' to generate a summary of 
  # Dataset Summary"
print("Crime Dataset Columns")
print(crime_data.columns)

print("Crime Dataset Summary")
print(crime_data.info())

print("Crime Dataset Example with Values")
print(crime_data.head(5))

#%%% Cleaning the data: Eliminate Missing Values in Columns
print(crime_data.columns[crime_data.isnull().any()].tolist())

#Use .dropna to eliminate missing values
crime_data = crime_data.dropna()

#%% Selecting Specific Columns for Data Analysis
df = crime_data[['Date', 'Year', 'Primary Type','Description', 'Location Description']]
print(df.columns)
print(df.info())

df.to_csv("df.csv",index = False, header = True, sep = ',', encoding = 'utf-8')

#%% Building a DataFrame for types of Crime committed, real count and percentage 

crime_type = pd.DataFrame(df['Primary Type'].value_counts()).reset_index() 
crime_type.columns = ['Crime Type', 'Count']
crime_type_value_counts = pd.DataFrame(df['Primary Type'].value_counts().reset_index())
crime_type_value_counts.columns = ['Crime Type', 'Count']
crime_type_value_counts['Percentage'] = (crime_type_value_counts['Count']/crime_type_value_counts['Count'].sum()) * 100
print(crime_type_value_counts)

print(crime_type_value_counts.head(10))

#%% Merging the two dataframes with pd.concat 

result = [df, crime_type_value_counts]
df_final = pd.concat(result)

print(df_final.head())

print(df_final.info())


# df_final = pd.concat([df, crime_type_value_counts])
# print(df_final)








             


        
        