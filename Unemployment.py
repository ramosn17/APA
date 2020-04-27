#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 02:54:15 2020

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

print("Unemployment Data Information")


#Read CSV File to datframe unemployment
unemployment = pd.read_csv("unemployment.csv")                           
pd.set_option('display.max_columns', None)
print(unemployment.head(5))

#Summarize data for unemployment

print(unemployment.info())
