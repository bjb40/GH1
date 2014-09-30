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
#"Mexico":2310,
"Belize":2045,
"Guatemala":2250,
#"Honduras":2280, 
#"El Salvador":2190,
#"Nicaragua":2340,
#"Costa Rica":2140,
#"Cuba":2150,
#"Jamaica":2290,
#"Haiti":2270,
#"Dominican Republic":2170,          
#"Bahamas":2030
}


#Load in ICD-9 data for each of the countries listed above
print "Loading data from '" + dirs["rawdat"] + "'."

#unzip file and read csv
icd9zip = zipfile.ZipFile(dirs["rawdat"] + "/morticd09.zip")
icd9raw = icd9zip.open('Morticd9','rU')

icd9allcause = []
icd9sub = []
for row in csv.DictReader(icd9raw):
    for i in countries:
        if int(row["Country"]) == int(countries[i]):
            row["Country_Name"] = i
            icd9sub.append(row)
            #tabulate causes
            if row["Cause"] == "B00":
                icd9allcause.append(row)

#print (len(icd9allcause), len(icd9sub))

# icd9 Basic tabulation keys for cause
#B00 = all causes
'''
Heart Diseases
B26	401-405	Hypertensive disease
   B260	402, 404	Hypertensive heart disease
   B269		Remainder of B26
B27	410-414	Ischaemic heart disease
   B270	410	Acute myocardial infarction
   B279		Remainder of B27
B28	415-429	Diseases of pulmonary circulation and other forms of heart disease
   B280	415.1	Pulmonary embolism
   B281	427	Cardiac dysrhythmias
   B289		Remainder of B28
B29	430-438	Cerebrovascular disease
   B290	430	Subarachnoid haemorrhage 
   B291	431, 432	Intracerebral and other intracranial haemorrhage
   B292	433, 434	Cerebral infarction
   B293	436	Acute but ill-defined cerebrovascular disease
   B294	437.0	Cerebral atherosclerosis
   B299		Remainder of B29
B30	440-459	Other diseases of the circulatory system
   B300	440	Atherosclerosis
   B301	444	Arterial embolism and thrombosis
   B302	441-443, 446-448	Other diseases of arteries, arterioles and capillaries
'''

#Load ICD-10 data for countries

#@@@@@@@@@@@@@@@@@@@
#TO BE DONE SHORTLY
#@@@@@@@@@@@@@@@@@@@

#Load population data
popzip = zipfile.ZipFile(dirs["rawdat"] + "/Pop.zip")
popraw = popzip.open('pop','rU')

popsub = []
for row in csv.DictReader(popraw):
    for i in countries:
        if int(row["Country"]) == int(countries[i]):
            popsub.append(row)

print popsub[1].keys()

#put them all together and calculate rates


#@@@@@@@@@@@@@@@@@@@@@@@
#3 
#@@@@@@@@@@@@@@@@@@@@@@@
