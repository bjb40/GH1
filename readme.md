---
author: Bryce Bartlett
title: Analysis code of CVD/CHD in Belize
date: October 2, 2014
---

##WHO Mortality Database#

Data comes from raw files in the World Health Organization Mortality Database [http://www.who.int/healthinfo/statistics/mortality_rawdata/en/](http://www.who.int/healthinfo/statistics/mortality_rawdata/en/) (downloaded 9/17/2014). Python code to clean the data and publish to plot.ly are contained in "code." 

##Selected Codes#
The following are excerpts of the table form WHO documentaiton; all statistics presented were limited to these codes.

ICD-9 Codes Selected:

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


ICD-10 Codes Selected:

1064	I00-I99	Diseases of the circulatory system
1065	I00-I09	Acute rheumatic fever and chronic rheumatic heart diseases
1066	I10-I13	Hypertensive diseases
1067	I20-I25	Ischaemic heart diseases
1068	I26-I51	Other heart diseases
1069	I60-I69	Cerebrovascular diseases
1070	I70	Atherosclerosis
1071	I71-I99	Remainder of diseases of the circulatory system
