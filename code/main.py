'''
!/usr/bin/python
Python 2.7
Main file for Global Health Analysis
Bryce Bartlett

This project analyzes NCD burden in select Central American and Carribean countries. Underaken primarily to fulfill requirement of NCD class regarding low and middle income countries. Will also look to institutional/biomedicalization changes for countries of interest.

Analysis will use python and R, analyze changing rates of NCDs, and changes in health care institutions/population risk factors (like smoking). Finally, I will include Hierarchical bayesian projections. Code Segments are numbered and outlined by' @@@@.'

'''

#@@@@@@@@@@@@@@@@@@@@@@@
#1 assign dependencies and import config variables
#@@@@@@@@@@@@@@@@@@@@@@

import csv
import pandas as pd
import numpy as np
import scipy as sp
import sys,os

print ('sys.argv[0]',sys.argv[0])

curdir = os.path.dirname(os.path.realpath(sys.argv[0]))
print('currentdir',curdir)

workdir = os.getcwd()

print ('workdir',workdir)

#@@@@@@@@@@@@@@@@@@@@@@@
#2 import raw data and prep working dataset
#@@@@@@@@@@@@@@@@@@@@@@@



#@@@@@@@@@@@@@@@@@@@@@@@
#3 
#@@@@@@@@@@@@@@@@@@@@@@@
