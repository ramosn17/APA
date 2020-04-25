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

#Read the CSV file to a Dataframe entitled Weather

weather = pd.read_csv("weather.csv")
print(weather.columns)
print(weather.head(5))
print(weather.info())


#Grouped Weather Data on 'Date' key

grouped_weather = weather.groupby(['Date']).mean().reset_index()

grouped_weather = grouped_weather[['Date', 'Max TemperatureF', 'Mean TemperatureF',
       'Min TemperatureF','Max Humidity', ' Mean Humidity', ' Min Humidity',
       'PrecipitationIn']]

print(grouped_weather.head(5))

print(grouped_weather.info())
print(grouped_weather.columns)

weather_columns_list = ['Max TemperatureF', 'Mean TemperatureF',
       'Min TemperatureF', 'Max Humidity', ' Mean Humidity', ' Min Humidity',
       ' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', 'PrecipitationIn']







