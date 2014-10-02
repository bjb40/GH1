'''
!/usr/bin/python
Python 2.7
Main file for Global Health Analysis
Bryce Bartlett

This project analyzes NCD burden in select Central American and Carribean countries. Underaken primarily to fulfill requirement of NCD class regarding low and middle income countries. Will also look to institutional/biomedicalization changes for countries of interest.
9/29/2014

'''

#Analysis will use python and R, analyze changing rates of NCDs, and changes in health care institutions/population risk factors (like smoking). Finally, I will include Hierarchical bayesian projections. Code Segments are numbered and outlined by' @@@@.'


#@@@@@@@@@@@@@@@@@@@@@@@
#1 assign dependencies and import config variables for data locations
#@@@@@@@@@@@@@@@@@@@@@@

import csv, sys, os, zipfile, re
import pandas as pd
import numpy as np
import scipy as sp
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *


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

    with open(curdir + '\config.txt', 'rb') as csvfile:
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
#"Guatemala":2250,
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
print "\n\nLoading ICD9 data from '" + dirs["rawdat"] + "'."

#unzip file and read csv
icd9zip = zipfile.ZipFile(dirs["rawdat"] + "/morticd09.zip")
icd9raw = icd9zip.open('Morticd9','rU')

#prepare regular expression to catch diseases B26-B29 or B30
cvd = re.compile(r'B2[6-9]$|B30$')

icd9cvd = []
icd9allcause = []
icd9sub = []
for row in csv.DictReader(icd9raw, delimiter=',', quotechar="'"):
    for i in countries:
        if int(row["Country"]) == int(countries[i]):
            row["Country_Name"] = i
            icd9sub.append(row)
            #tabulate all causes
            if row["Cause"] == "B00":
                icd9allcause.append(row)
            #tabulate heart disease causes
            elif cvd.search(row["Cause"]):
                icd9cvd.append(row)

'''
Put this into a "note".
B00 All cause


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
print "\n\nLoading ICD10 data from '" + dirs["rawdat"] + "'."

#unzip file and read csv
icd10zip = zipfile.ZipFile(dirs["rawdat"] + "/morticd10.zip")
icd10raw = icd10zip.open('Morticd10','rU')

#prepare regular expression to catch diseases from I10-I99
#note that unlike ICD9, there is no entry for Belize regarding all-cause
cvd10 = re.compile(r'I[1-9]')

icd10cvd = []
icd10sub = []
for row in csv.DictReader(icd10raw, delimiter=',', quotechar="'"):
    for i in countries:
        if int(row["Country"]) == int(countries[i]):
            row["Country_Name"] = i
            icd10sub.append(row)
            #tabulate heart disease causes
            if cvd10.search(row["Cause"]):
                icd10cvd.append(row)

'''
1064	I00-I99	Diseases of the circulatory system
1065	I00-I09	Acute rheumatic fever and chronic rheumatic heart diseases
1066	I10-I13	Hypertensive diseases
1067	I20-I25	Ischaemic heart diseases
1068	I26-I51	Other heart diseases
1069	I60-I69	Cerebrovascular diseases
1070	I70	Atherosclerosis
1071	I71-I99	Remainder of diseases of the circulatory system

'''


print "\n\nLoading Population data from '" + dirs["rawdat"] + "'."
#Load population data
popzip = zipfile.ZipFile(dirs["rawdat"] + "/Pop.zip")
popraw = popzip.open('pop','rU')

popsub = []
for row in csv.DictReader(popraw):
    for i in countries:
        if int(row["Country"]) == int(countries[i]):
            popsub.append(row)


#calculate rates from disparate lists by first iterating over db
print "\n\n Calculating Rates . . ."

#NOTE - for countries with an admin or subdiv content, the code needs to be edited to take into consideration
def mf(cell):
    '''Checks for missing, assigns -9 to missing otherwise converts to float'''
    if cell.isdigit():
        return(float(cell))
    else:
        return(-9.)

def rate(num,den):
    '''Converts strings to number and divides num by den'''
    if isinstance(num,str) == True:
        num = mf(num)
    if isinstance(den,str) == True:
        den = mf(den)
    if num < 0 or den < 0:
        return(-9.)
    else:
        return(num/den)


def sumcells(vals):
    '''Converts a list of strings to numbers if they include digits '''
    tot = 0
    for i in vals:
        if i.isdigit():
            tot += float(i)
    return(tot)

dat = []
for n in icd9cvd:
    temp = {}
    for d in popsub:
        if n["Country"] == d["Country"] and n["Year"] == d["Year"] and n["Sex"] ==  d["Sex"]:
            #select and clean variables
            temp["Country_Name"] = n["Country_Name"]
            temp["Country"] = n["Country"]
            temp["Year"] = n["Year"]
            if int(n["Sex"]) == 1:
                temp["Male"] = 1
            else:
                temp["Male"] = 0
            if int(n["Frmat"]) < 4 and int(d["Frmat"]) < 4: 
                temp["DeathsLAST"] = sumcells([n["Deaths21"],n["Deaths22"],n["Deaths23"],n["Deaths24"],n["Deaths25"]])
                temp["PopLAST"] = sumcells([d["Pop21"],d["Pop22"],d["Pop23"],d["Pop24"],d["Pop25"]])
                temp["Cause"] = n["Cause"]
                temp["15-19 Mx"] = rate(n["Deaths9"],d["Pop9"])
                temp["20-24 Mx"] = rate(n["Deaths10"],d["Pop10"])
                temp["25-29 Mx"] = rate(n["Deaths11"],d["Pop11"])
                temp["30-34 Mx"] = rate(n["Deaths12"],d["Pop12"])
                temp["35-39 Mx"] = rate(n["Deaths13"],d["Pop13"])
                temp["40-44 Mx"] = rate(n["Deaths14"],d["Pop14"])
                temp["45-49 Mx"] = rate(n["Deaths15"],d["Pop15"])
                temp["50-54 Mx"] = rate(n["Deaths16"],d["Pop16"])
                temp["55-59 MX"] = rate(n["Deaths17"],d["Pop17"])
                temp["60-64 Mx"] = rate(n["Deaths18"],d["Pop18"])
                temp["65-69 Mx"] = rate(n["Deaths19"],d["Pop19"])
                temp["70-74 Mx"] = rate(n["Deaths20"],d["Pop20"])
                temp["75+ Mx"] = rate(temp["DeathsLAST"],temp["PopLAST"])
 #           keepvals = n.update(d)
 #           if re.search(r"Deaths|Pop",)
            dat.append(temp)
            break

outf = dirs["output"] + "/datfile.csv"
#write rates to csv - pandas dataframe may be better???
fnames = dat[0].keys()
with open(outf,"wb") as f:
    writer = csv.DictWriter(f ,delimiter=',',  fieldnames = fnames)
    writer.writeheader()
    for row in dat:
        writer.writerow(row)
f.close()

#@@@@@@@@@@@@@@@@@@@@@@@
#3 Analyze data from working dataset (can be used solely from import)
#@@@@@@@@@@@@@@@@@@@@@@@

pw = str(raw_input("Plot.ly sign in key: "))
py.sign_in("bjb40", pw)

dat = pd.read_csv(outf)
groupdat = dat.groupby(["Male","Year"])
years = dat.groupby("Year").groups.keys()


Trace1 = Scatter(
    name = "Female50-54",
    y=groupdat["50-54 Mx"].sum().ix[0:0],
    x=sorted(years, key=int),
    xaxis='x1',
    yaxis='y1'
 )


Trace2 = Scatter(
    name = "Male",
    y=groupdat["50-54 Mx"].sum().ix[1:1],
    x=sorted(years,key=int),
    xaxis='x2',
    yaxis='y2'
 )

Trace3 = Scatter(
    name = "Female55-59",
    y=groupdat["55-59 MX"].sum().ix[0:0],
    x=sorted(years, key=int),
    xaxis='x3',
    yaxis='y3'
 )


Trace4 = Scatter(
    name = "Male",
    y=groupdat["55-59 MX"].sum().ix[1:1],
    x=sorted(years,key=int),
    xaxis='x4',
    yaxis='y4'
 )

Trace5 = Scatter(
    name = "Female 60-64",
    y=groupdat["60-64 Mx"].sum().ix[0:0],
    x=sorted(years,key=int),
    xaxis='x5',
    yaxis='y5'
)


Trace6 = Scatter(
    name = "Male 60-64",
    y=groupdat["60-64 Mx"].sum().ix[1:1],
    x=sorted(years,key=int),
    xaxis='x6',
    yaxis='y6'
)


data = Data([Trace1,Trace2,Trace3,Trace4,Trace5,Trace6])
fig=tls.get_subplots(rows=3, columns=2)
layout = Layout(
    title="Figure 1. Rate of Cardiac Deaths Belize, 1980-1995",
    yaxis1=YAxis(title="50-54 Mx"),
    yaxis3=YAxis(title="55-59 Mx"),
    yaxis5=YAxis(title="60-64 Mx"),
    xaxis3=XAxis(title="Male"),
    xaxis4=XAxis(title="Female"),
    showlegend=False
)
fig['data'] += data
fig['layout'].update(layout)


plot_url = py.plot(fig, filename='Global_Health_Fig1', world_readable=False)
 
#py.image.save_as({'data':data}, dirs["output"] + '/test.png', format='png')
