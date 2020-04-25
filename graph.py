#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 04:18:20 2020

@author: user
"""

import operator
from os import listdir
import matplotlib.pyplot as plt; plt.rcdefaults()
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


crime_data = pd.read_csv("Crimes_-_2001_to_present.csv", low_memory= False)
df = crime_data[['Date', 'Primary Type','Description', 'Location Description','Arrest']]
print(df.columns)
print(df.info())





 # Sample: Building a DataFrame for types of Crime committed, real count and percentage 

crime_type = pd.DataFrame(df['Primary Type'].value_counts()).reset_index() 
crime_type.columns = ['Crime Type', 'Count']
crime_type_value_counts = pd.DataFrame(df['Primary Type'].value_counts().reset_index())
crime_type_value_counts.columns = ['Crime Type', 'Count']
crime_type_value_counts['Percentage'] = (crime_type_value_counts['Count']/crime_type_value_counts['Count'].sum()) * 100
print(crime_type_value_counts.head(10))


#Bar Graph for Crime Count, Primary Type

objects = ('THEFT', 'BATTERY', 'CRIMINAL DAMAGE', 'ASSAULT', 'OTHER', 'DECEPTIVE PRACT','NARCOTICS',
           'BURGLARY', 'ROBBERY', 'MOTOR  THEFT')
fontsize = 10
y_pos = np.arange(len(objects))
performance = [230626, 185410,107082, 71307, 62521,
               61834,53384, 47299, 39923, 38975]

plt.bar(y_pos, performance, align='center', alpha=1.0)
plt.xticks(y_pos, objects)
plt.ylabel('Count')
plt.title(' Crime Count in Chicago by Type')
plt.show()


#Pie Chart for Crime Count, Primary Type

labels = ['THEFT', 'BATTERY', 'CRIMINAL DAMAGE', 'ASSAULT', 'OTHER OFFENSE', 
          'DECEPTIVE PRACTICE','NARCOTICS','BURGLARY', 'ROBBERY', 'MOTOR VEHICLE THEFT']
sizes = [23.594877,18.968920, 10.955342, 7.295274, 6.396396, 6.326111,5.461608,4.839064,4.084441, 3.987453]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink', 'green', 'black', 'purple', 'orange', 'red']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
explode = (0.1, 0, 0, 0,0,0,0,0,0,0 )  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

##Crime Count By Location Type

print(df.columns)
print(df.head(5))
print("Location Description Includes ")
location_description_value_counts = pd.DataFrame(df['Location Description'].value_counts().reset_index())
location_description_value_counts.columns = ['Location Description', 'Count']
location_description_value_counts['Percentage'] = (location_description_value_counts['Count']/location_description_value_counts['Count'].sum()) * 100
print(location_description_value_counts.head(10))

#Bar Graph Crime Count By Location Type

objects = ['STREET', 'RESIDENCE', 'APARTMENT', 'SIDEWALK', 'OTHER','PARKING LOT/GARAGE(NON.RESID.)', 'SMALL RETAIL STORE',
          'RESTAURANT', 'ALLEY', 'RESIDENTIAL YARD (FRONT/BACK)']
y_pos = np.arange(len(objects))
performance = [222780 ,  162257,125808 ,86510 ,41279  , 28829  ,23393 , 22746,20017, 19764 ]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Count')
plt.title('Total Crime Count By Location Type')
plt.show()

#Pie Chart For Crime Percentage By Location Type
labels = ['STREET', 'RESIDENCE', 'APARTMENT', 'SIDEWALK', 'OTHER','PARKING LOT/GARAGE(NON.RESID.)', 'SMALL RETAIL STORE',
          'RESTAURANT', 'ALLEY', 'RESIDENTIAL YARD (FRONT/BACK)']
sizes = [22.792169, 16.600184, 12.871161, 8.850662, 4.223171,  2.949436, 2.393290,
         2.327097,2.047899,  2.022015]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'cyan', 'brown', 'black', 'purple', 'orange', 'red']

patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
explode = (0.1, 0, 0, 0,0,0,0,0,0,0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Highest Occurences of Crime By Location Type, as a percentage of the total crime count" , fontsize = 12) 
plt.axis('equal')
plt.show()
# plt.show()







