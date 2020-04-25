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

df_final = pd.read_csv('df_final.csv')
weather = pd.read_csv('weather.csv')
unemployment = pd.read_csv('unemployment3.csv')
#%%
print(unemployment.info())


#Utilize pd.merge function to merge crime type, weather and unemployment data on Date key
analysis_dataset = pd.merge(df_final, weather,on=['Date'])
analysis_dataset = pd.merge(analysis_dataset,unemployment, on=['Date'])

print("Analysis Dataset Information")
print(analysis_dataset.head(5))

analysis_dataset.to_csv("crime_info1.csv")

print(analysis_dataset.columns)
print(analysis_dataset.info())
#%%
grouped_unemp = analysis_dataset.groupby(["Primary Type", "Unemployment"]).mean()




