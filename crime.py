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
from worldcloud import WordCloud, STOPWORDS, ImageColorGenerator
import plotly.graph_objs as go
import plotly.express as px


##Import the datafile as crime_data

crime_data = pd.read_csv("Crimes_-_2001_to_present.csv", low_memory= False)

##Review columns in dataset

print("Crime Dataset Columns")
print(crime_data.columns)

print("Crime Dataset Summary")
print(crime_data.info())

print("Crime Dataset Example with Values")
print(crime_data.head(5))


#Cleaning the data: Eliminate Missing Values in Columns
print(crime_data.columns[crime_data.isnull().any()].tolist())

#Use .dropna to eliminate missing values
crime_data = crime_data.dropna()


#Selecting Specific Columns for Data Analysis
df = crime_data[['Date', 'Primary Type','Description', 'Location Description','Arrest']]
print(df.columns)
print(df.info())


 # Sample: Building a DataFrame for types of Crime committed, real count and percentage 

crime_type = pd.DataFrame(df['Primary Type'].value_counts()).reset_index() 
crime_type.columns = ['Crime Type', 'Count']
crime_type_value_counts = pd.DataFrame(df['Primary Type'].value_counts().reset_index())
crime_type_value_counts.columns = ['Crime Type', 'Count']
crime_type_value_counts['Percentage'] = (crime_type_value_counts['Count']/crime_type_value_counts['Count'].sum()) * 100



df_final = pd.concat([df, crime_type_value_counts])
print(df_final)


df_final.to_csv("df_final.csv", index = False, header = True, sep = ',', encoding = 'utf-8')


#Exploratory Analysis using the groupby function

df_final['major'] =  df_final['Primary Type']+ ',' + df['Description']

mfrequent_crimes = df_final.groupby(['major'])['Arrest'].count()
mfrequent_crimes = pd.DataFrame(mfrequent_crimes).nlargest(20, 'Arrest').reset_index()
mfrequent_crimes = list(mfrequent_crimes['major'])             
print(mfrequent_crimes)     

             


# fig = px.bar(crime_type_value_counts, x="Crime Type", y="Count", color="Crime Type", title="Crime Type Bar Chart")
# fig.show()
# fig = px.pie(crime_type_value_counts, values='Percentage', names='Crime Type', title="Crime Type Pie Chart",color_discrete_sequence=px.colors.sequential.RdBu)
# fig.show()

# import matplotlib.pyplot as plt
# #Data to Plot

# labels = 
        
        