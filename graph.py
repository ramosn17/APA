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
from os import path
from PIL import Image
import pylab as pl

#%%

crime_data = pd.read_csv("Crimes_-_2001_to_present.csv", low_memory= False)
df = crime_data[['ID', 'Date', 'Year','Primary Type','Description', 'Location Description']]
print(df.columns)
print(df.info())
print(df.head(5))


 #  Building a DataFrame for types of Crime committed, real count and percentage 

crime_type = pd.DataFrame(df['Primary Type'].value_counts()).reset_index() 
crime_type.columns = ['Crime Type', 'Count']
crime_type_value_counts = pd.DataFrame(df['Primary Type'].value_counts().reset_index())
crime_type_value_counts.columns = ['Crime Type', 'Count']
crime_type_value_counts['Percentage'] = (crime_type_value_counts['Count']/crime_type_value_counts['Count'].sum()) * 100
print(crime_type_value_counts.head(10))


#%%

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

#%%
##Crime Count By Location Type. We will take the top ten crime count values by location and 
#plot the data for a clearer visaulization. The subsequent bar graph will show where the highest number of
#crimes occur-first in the street, residence and apartment. 

print(df.columns)
print(df.head(5))
print("Location Description Includes ")
location_description_value_counts = pd.DataFrame(df['Location Description'].value_counts().reset_index())
location_description_value_counts.columns = ['Location Description', 'Count']
location_description_value_counts['Percentage'] = (location_description_value_counts['Count']/location_description_value_counts['Count'].sum()) * 100
print(location_description_value_counts.head(10))

#Bar Graph Crime Count By Location Type

objects = ['STREET', 'RESIDENCE', 'APT', 'SIDEWALK', 'OTHER','PARKING LOT', 'SM RETAIL',
          'RESTAURANT', 'ALLEY', 'RES. YARD']
y_pos = np.arange(len(objects))
performance = [222780 ,  162257,125808 ,86510 ,41279  , 28829  ,23393 , 22746,20017, 19764 ]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Count')
plt.title('Total Crime Count By Location Type')
plt.show()

#%%
#Pie Chart For Crime Percentage By Location Type. Same data and results as the bar graph, but slightly more aesthetic
#and clear. Also offers some diversity in the visuals. 

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

#%% Building on this initial set of graph development, we can use the Datetime module
#to convert the 'Date' column into the m/d/Y format to graph crimes by month and year in pandas.
#We can use this index to graph crimes per month and day over the period of 2001-2020. These graphs will provide
#a closer visual for overall crime type trends across the entire period. 

df.Date = pd.to_datetime(df.Date, format='%m/%d/%Y %I:%M:%S %p')

df.index = pd.DatetimeIndex(df.Date)


#%%Utilize plotly  to establish a record of crimes per month.
#This chart will exhibit a 'periodic' pattern in crimes from 2001-2020.
#Overall, the chart shows that crime is decreasing across the period, but a deeper 
#look can be executed to compare crimes from 2020 to 2019 to determine whether the crime rate has decreased
#from a given year, or stays the same. This graph shows an overall decrease in crimes from 2001-2020, with periodic decreases
#near the end of each year (winter months) and increases mid to later-mid portion of the year (Spring/Summer). 



plt.figure(figsize=(11,5))
df.resample('M').size().plot(legend=False)
plt.title('Number of crimes per Year (2001 - 2020)')
plt.xlabel('Years')
plt.ylabel('Number of crimes')
plt.show()

#%% This graph will provide a clearer visual for changes in crime from 2019 to 2020. 
#We can observe a decrease in overall crime from 2002 to 2016, after which the number of 
#crimes remains relatively constant from 2016-2019, with a slight decrease from 2019-2020. 

plt.figure(figsize=(11,4))
df.resample('D').size().rolling(365).sum().plot()
plt.title('Rolling sum of all crimes from 2001 - 2020')
plt.ylabel('Number of crimes')
plt.xlabel('Days')
plt.show()


#%% These graphs exhibit the trend in crimes by type from 2001-2020. While the majority of crimes 
#by time are decreasing, the trend is actually the opposite for weapons violations, interference with a public officer,
#concealed carry violations and other narcotics violations. The sharp increases in 'other narcotics violations, weapns and actions against
#police officers serves to mitigate (or account for) the marginal decrease in overall crimes from 2019-20.  

crimes_count_date = df.pivot_table('ID', aggfunc=np.size, columns='Primary Type', index= df.index.date,fill_value=0)
print(crimes_count_date)

crimes_count_date.index = pd.DatetimeIndex(crimes_count_date.index)
plot = crimes_count_date.rolling(365).sum().plot(figsize =(12,30), subplots=True, layout = (-1,3), sharex=False, sharey=False)


#%% Same representation as the previous bar graph that integrated highest ten values for crime type. This graph provides
#a more granular representation of the entire crime catergory. Given the previous breakdown by crime type, we can predict increases in the 
#number of crimes for conealed carry, interference w/ public officer, weapons violations and narcotics in subsequent data post-2020. 
plt.figure(figsize=(8,10))
df.groupby([df['Primary Type']]).size().sort_values(ascending=True).plot(kind='barh')
plt.title('Number of crimes by type')
plt.ylabel('Crime Type')
plt.xlabel('Number of crimes')
plt.show()
