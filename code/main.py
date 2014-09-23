'''
!/usr/bin/python
Python 2.7
Main file for Global Health Analysis
Bryce Bartlett

This project analyzes NCD burden in select Central American and Carribean countries. Underaken primarily to fulfill requirement of NCD class regarding low and middle income countries. Will also look to institutional/biomedicalization changes for countries of interest.

'''

#Analysis will use python and R, analyze changing rates of NCDs, and changes in health care institutions/population risk factors (like smoking). Finally, I will include Hierarchical bayesian projections. Code Segments are numbered and outlined by' @@@@.'


#@@@@@@@@@@@@@@@@@@@@@@@
#1 assign dependencies and import config variables for data locations
#@@@@@@@@@@@@@@@@@@@@@@

import csv
import pandas as pd
import numpy as np
import scipy as sp
import sys,os
import zipfile
import io

print str(locals()['__doc__'])

dirs = {}

if sys.argv[0] == '':
    print "Cannot load data paths - close and execute from command line, or input directories below.\n\n"
    dirs["work"] = str(raw_input("Working Directory: "))
    dirs["rawdat"] = str(raw_input("Directory of raw data: "))
    dirs["output"] = str(raw_input("Directory for analysis output: "))

else:
    curdir = os.path.dirname(os.path.realpath(sys.argv[0]))
    print "Loading config file from " + str(curdir)

    with open(curdir + '\config.txt', 'r') as csvfile:
        configs = csv.reader(csvfile)
        for i in configs:
            dirs[str(i[0])] = str(i[1])


#@@@@@@@@@@@@@@@@@@@@@@@
#2 import raw data and prep working dataset
#@@@@@@@@@@@@@@@@@@@@@@@

# select countries and country number
    
countries = {
"Mexico":2310,
"Belize":2045,
"Guatemala":2250,
#"Honduras":2280, 
#"El Salvador":2190,
#"Nicaragua":2340,
#"Costa Rica":2140,
"Cuba":2150,
"Jamaica":2290,
#"Haiti":2270,
#"Dominican Republic":2170,          
"Bahamas":2030
}


#Load in ICD-9 data for each of the countries listed above
print "Loading data from '" + dirs["rawdat"] + "'."

#unzip file and read csv
icd9zip = zipfile.ZipFile(dirs["rawdat"] + "/morticd09.zip")
icd9raw = icd9zip.open('Morticd9','rU')

icd9sub = []

counter = 0
for row in csv.DictReader(icd9raw):

    counter += 1
#    if counter < 10000:
    for i in countries:
        if int(row["Country"]) == int(countries[i]):
            icd9sub.append(row)


for row in icd9sub:
    print(row["Admin1"],row["SubDiv"])




#@@@@@@@@@@@@@@@@@@@@@@@
#3 
#@@@@@@@@@@@@@@@@@@@@@@@
