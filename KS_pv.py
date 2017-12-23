#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 22:07:22 2017

@author: SR
"""

 
#
# Fichier: excel-fr. acces au site ===> pyhttp://re.jrc.ec.europa.eu/pvg_tools/en/tools.html#HR ==> télechargement du fichier csv météo du site.

import os
import csv
import time
import datetime
import locale
import operator
import numpy as np
import pandas as  pd
from datetime import datetime
from dateutil.parser import parse
from datetime import timedelta

Année_start='2016'
Année_end='2017'
JM_start='12-19 00:00'

date_ref=pd.date_range('01-01-2001','01-01-2002' , freq="H", name='Date', tzinfo='UTC')
NewDate_start=JM_start+'-'+'2001'

#Mise en forme du dataframe Pv à partir de JRC (ressource Web) 

PvBrut = pd.read_csv("/Users/srmac/Dropbox/Kepler/KeplerSoft/Fichier.csv JRC/Timeseries_47.596_1.818_CM__1kWp_crystSi_14_35deg_-8deg_2007_2016.csv", sep = ','
                     ,engine='python',skiprows=10,skipfooter=11).drop(['G_i','As','int.'],axis=1)
PvBrut['Date']=pd.to_datetime(PvBrut['Date'], format='%Y%m%d:%H%M',utc=True)


PvBrut['Date'] = PvBrut.Date.dt.tz_localize('UTC').dt.tz_convert('Europe/Paris')+timedelta(minutes=5)
PvBrut['Date_sans_Année']=PvBrut['Date'].apply(lambda x: x.strftime('%m-%d %H:%M'))

gpv_bisex=PvBrut['EPV'].groupby(PvBrut['Date_sans_Année']).mean()
gtamb_bisex=PvBrut['Tamb'].groupby(PvBrut['Date_sans_Année']).mean()
gw10_bisex=PvBrut['W10'].groupby(PvBrut['Date_sans_Année']).mean()

gpv=gpv_bisex.drop(['02-29 00:00','02-29 01:00','02-29 02:00','02-29 03:00','02-29 04:00','02-29 05:00',
                  '02-29 06:00','02-29 07:00','02-29 08:00','02-29 09:00','02-29 10:00','02-29 11:00',
                  '02-29 12:00','02-29 13:00','02-29 14:00','02-29 15:00','02-29 16:00','02-29 17:00',
                  '02-29 18:00','02-29 19:00','02-29 20:00','02-29 21:00','02-29 22:00','02-29 23:00'])
gtamb= gtamb_bisex.drop(['02-29 00:00','02-29 01:00','02-29 02:00','02-29 03:00','02-29 04:00','02-29 05:00',
                  '02-29 06:00','02-29 07:00','02-29 08:00','02-29 09:00','02-29 10:00','02-29 11:00',
                  '02-29 12:00','02-29 13:00','02-29 14:00','02-29 15:00','02-29 16:00','02-29 17:00',
                  '02-29 18:00','02-29 19:00','02-29 20:00','02-29 21:00','02-29 22:00','02-29 23:00'])

gpv1=gpv[JM_start:]
gtamb1=gtamb[JM_start:]
index1=[]
for i in range(len(gpv1)):
     index1.append( Année_start+'-'+gpv1.index[i])

pvf1=pd.DataFrame({'Pui_PV':gpv1.values,'Tamb':gtamb1.values}, index=index1)


gpv2=gpv.truncate(after=JM_start)
gpv2=gpv2[:-1]
gtamb2=gtamb.truncate(after=JM_start)
gtamb2=gtamb2[:-1]
index2=[]
for i in range(len(gpv2)):
     index2.append( Année_end+'-'+gpv2.index[i])

pvf2=pd.DataFrame({'Pui_PV':gpv2.values,'Tamb':gtamb2.values}, index=index2)

Pv=pd.concat([pvf1,pvf2])
Pv.index = pd.to_datetime(Pv.index)









