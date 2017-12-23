#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:21:59 2017

"""
# Fichier: excel-fr. acces au site ===> pyhttp://re.jrc.ec.europa.eu/pvg_tools/en/tools.html#HR ==> télechargement du fichier csv météo du site.

import os
import csv
import time
import datetime 
import locale
import operator
import numpy as np
import pandas as  pd
from datetime import *
import copy
from KS_pv import Pv



locale.setlocale(locale.LC_ALL,'fr_FR')

P1d='19/12/2016'
P1f='17/1/2017'
HPH1=21718
HCH1=5884
HPB1=0
HCB1=0

P2d='18/1/2017'
P2f='12/2/2017'
HPH2=20457
HCH2=5150
HPB2=0
HCB2=0

P3d='13/2/2017'
P3f='9/3/2017'
HPH3=21094
HCH3=5641
HPB3=0
HCB3=0

P4d='10/3/2017'
P4f='9/4/2017'
HPH4=16009
HCH4=3124
HPB4=2151
HCB4=884

P5d='10/4/2017'
P5f='9/5/2017'
HPH5=0
HCH5=0
HPB5=15290
HCB5=3530

P6d='10/5/2017'
P6f='9/6/2017'
HPH6=0
HCH6=0
HPB6=6453
HCB6=1701

P7d='10/6/2017'
P7f='9/7/2017'
HPH7=0
HCH7=0
HPB7=8800
HCB7=2319

P8d='10/7/2017'
P8f='18/8/2017'
HPH8=0
HCH8=0
HPB8=6453
HCB8=1701

P9d='19/8/2017'
P9f='17/9/2017'
HPH9=0
HCH9=0
HPB9=10688
HCB9=2203

P10d='19/9/2017'
P10f='17/10/2017'
HPH10=0
HCH10=0
HPB10=20269
HCB10=4697

P11d='18/10/2017'
P11f='20/11/2017'
HPH11=16073
HCH11=3402
HPB11=4196
HCB11=1294

P12d='21/11/2017'
P12f='18/12/2017'
HPH12=26467
HCH12=5417
HPB12=0
HCB12=0

tab = {} 

data={'Début':[P1d,P2d,P3d,P4d,P5d,P6d,P7d,P8d,P9d,P10d,P11d,P12d],'Fin':[P1f,P2f,P3f,P4f,P5f,P6f,P7f,P8f,P9f,P10f,P11f,P12f],'EHPH':[HPH1,HPH2,HPH3,HPH4,HPH5,HPH6,HPH7,HPH8,HPH9,HPH10,HPH11,HPH12],'EHCH':[HCH1,HCH2,HCH3,HCH4,HCH5,HCH6,HCH7,HCH8,HCH9,HCH10,HCH11,HCH12],'EHPB':[HPB1,HPB2,HPB3,HPB4,HPB5,HPB6,HPB7,HPB8,HPB9,HPB10,HPB11,HPB12],'EHCB':[HCB1,HCB2,HCB3,HCB4,HCB5,HCB6,HCB7,HCB8,HCB9,HCB10,HCB11,HCB12]}
df=pd.DataFrame(data,columns=['Début','Fin','EHPH','EHCH','EHPB','EHCB','Smax', 'Nbr_jours', 'Nbr_jours_ouvrés','Nbr_jours_chomés','Nbr_sam','Nbr_dim',
                             ],index=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12'])
hph=[]
hch=[]
hpb=[]
hcb=[]
Pui_HP=[]
Pui_HC=[]
##############################################################
#Fonction nombre de jour, jour ouvré, weekend, samedi dimanche *
############################################################## 
def nb_week(debut, fin):
    compteur = 0
    nb = nb_jours(debut, fin)
    for i in range(1, nb+1):
        new = date(*debut) + timedelta(days=i)
        if new.weekday() == 5 or new.weekday() == 6:
            compteur += 1
    return compteur
def nb_samedi(debut, fin):
    compteur = 0
    nb = nb_jours(debut, fin)
    for i in range(1, nb+1):
        new = date(*debut) + timedelta(days=i)
        if new.weekday() == 5 :
            compteur += 1
    return compteur

def nb_dimanche(debut, fin):
    compteur = 0
    nb = nb_jours(debut, fin)
    for i in range(1, nb+1):
        new = date(*debut) + timedelta(days=i)
        if new.weekday() == 6 :
            compteur += 1
    return compteur

 
def nb_jours(debut, fin):
    return abs(date(*debut)-date(*fin)).days+1


# Selection heure pleine et heure creuse en haute et basse saison.



month=Pv.index.month
weekday=Pv.index.weekday
hour=Pv.index.hour
selector_HP=((hour>6)  & (hour<=22)& (weekday<5 ))
selector_HC=(~selector_HP)


selector_HPH=((hour>=6)  & (hour<=22) ) & (((3>=month) & (month>=1))|((month>=11) & (month<=12)))
selector_HCH =(((hour<6)  & ( hour>=0)) | ((hour>=22)&( hour<=23))) & (((month>=1) & (month<=3))|((month>=11) & (month<=12))) 
selector_HPB=((hour>=6)  & (hour<=22) ) & ((month>=4) & (month<=10))
selector_HCB =(((hour<6)  & ( hour>=0)) | ((hour>=22)&( hour<=23))) & ((month>=4) & (month<=10))



############################
#Acquisition et mise sous tableau des données
############################

date_tuples = [tuple(map(int, i.split("/")))[::-1] for i in data['Début']]
df['Début']=date_tuples

date_tuples= [tuple(map(int, i.split("/")))[::-1] for i in data['Fin']]
df['Fin']=date_tuples

Nbr_jours=[nb_jours(df['Début'][i],df['Fin'][i]) for i in range (12)]
df['Nbr_jours']=Nbr_jours

Nbr_jours_ouvrés=[nb_jours(df['Début'][i],df['Fin'][i]) - nb_week(df['Début'][i],df['Fin'][i]) for i in range (12)]
df['Nbr_jours_ouvrés']= Nbr_jours_ouvrés  

Nbr_sam=[nb_samedi(df['Début'][i],df['Fin'][i]) for i in range(12)]
df['Nbr_sam']=Nbr_sam

Nbr_dim=[nb_dimanche(df['Début'][i],df['Fin'][i]) for i in range(12)]
df['Nbr_dim']=Nbr_dim

Nbr_jours_chomés=[nb_week(df['Début'][i],df['Fin'][i]) for i in range (12)]                   
df['Nbr_jours_chomés']=Nbr_jours_chomés


############################
#Acquisition et mise sous tableau des données
############################
for i in range(0,12):
    
    d=df['Début'][i]
    f=df['Fin'][i]
    
    if datetime (* d [ 0 : 3 ]).month>=4 and datetime (* f [ 0 : 3 ]).month<=10 and datetime (* d [ 0 : 3 ]).month<datetime (* f [ 0 : 3 ]).month:
         
         hcb.append(8*df.Nbr_jours_ouvrés[i]+24*df.Nbr_jours_chomés[i])
            
         hpb.append(16*df.Nbr_jours_ouvrés[i]) 
         
         hch.append(0)
         
         hph.append(0)
         
    elif datetime(* d [ 0 : 3 ]).month>=11 or datetime (* f [ 0 : 3 ]).month<=3:
        
         hch.append(8*df.Nbr_jours_ouvrés[i]+24*df.Nbr_jours_chomés[i])
         
        
         hph.append(16*df.Nbr_jours_ouvrés[i])
        
         hcb.append(0)
            
         hpb.append(0)
        
    elif datetime(* d [ 0 : 3 ]).month == 3 and datetime (* f [ 0 : 3 ]).month==4:
        
         
         Nbr_jours_ouvrés_avant31=nb_jours(d,(datetime(* f [ 0 : 3 ]).year,3,31))-nb_week(d,(datetime(* f [ 0 : 3 ]).year,3,31))
         Nbr_jours_chomés_avant31=nb_week(d,(datetime(* f [ 0 : 3 ]).year,3,31))
         Nbr_jours_ouvrés_post31=nb_jours((datetime(* f [ 0 : 3 ]).year,4,1),f)-nb_week((datetime(* f [ 0 : 3 ]).year,4,1),f)
         Nbr_jours_chomés_post31=nb_week((datetime(* f [ 0 : 3 ]).year,4,1),f)
         
         hch.append(8*Nbr_jours_ouvrés_avant31 + 24*Nbr_jours_chomés_avant31)
         hph.append(16*Nbr_jours_ouvrés_avant31)
         
         hcb.append(8*Nbr_jours_ouvrés_post31 + 24*Nbr_jours_chomés_post31)
         hpb.append(16*Nbr_jours_ouvrés_post31)
         
    elif datetime(* d [ 0 : 3 ]).month == 10 and datetime (* f [ 0 : 3 ]).month==11:
        
         Nbr_jours_ouvrés_avant31=nb_jours(d,(datetime(* f [ 0 : 3 ]).year,10,31))-nb_week(d,(datetime(* f [ 0 : 3 ]).year,10,31))
         Nbr_jours_chomés_avant31=nb_week(d,(datetime(* f [ 0 : 3 ]).year,10,31))
         Nbr_jours_ouvrés_post31=nb_jours((datetime(* f [ 0 : 3 ]).year,11,1),f)-nb_week((datetime(* f [ 0 : 3 ]).year,11,1),f)
         Nbr_jours_chomés_post31=nb_week((datetime(* f [ 0 : 3 ]).year,11,1),f)
         
         hch.append(8*Nbr_jours_ouvrés_avant31 + 24*Nbr_jours_chomés_avant31)
        
         hph.append(16*Nbr_jours_ouvrés_avant31)
         
         hcb.append(8*Nbr_jours_ouvrés_post31 + 24*Nbr_jours_chomés_post31)
            
         hpb.append(6*Nbr_jours_ouvrés_post31)
             
    Pui_HC.append((df.EHCH[i]+df.EHCB[i])/(hch[i]+hcb[i])) 
        
    Pui_HP.append(((df.EHPH[i]+df.EHPB[i])-(Pui_HC[i]*df.Nbr_jours_chomés[i]*16))/(df.Nbr_jours_ouvrés[i]*16) )
 
    dfPxHP=Pv[selector_HP]
    dfPxHP=dfPxHP[datetime(* d [ 0 : 3 ]):datetime(* f [ 0 : 3 ]).replace(hour=23)]
    dfPxHP['Pui_Conso']=Pui_HP[i]
    
    
    dfPxHC=Pv[selector_HC] 
    dfPxHC=dfPxHC[datetime(* d [ 0 : 3 ]):datetime(* f [ 0 : 3 ]).replace(hour=23)]
    dfPxHC['Pui_Conso']=Pui_HC[i]
    
    dfPx=pd.concat([dfPxHP,dfPxHC])
    dd=dfPx.sort_index()
    
##########################################################
 # Tableau de calcul Production-Consommation
#########################################################      
   
    tab[df.index[i]]=pd.DataFrame(dd) 
 ####################################################
##RESULTAT
###################################################   
frames  =  [ tab['P1'] ,  tab['P2'] ,  tab['P3'],tab['P4'] ,  tab['P5'] ,  tab['P6'],tab['P7'] ,  tab['P8'] ,  tab['P9'],tab['P10'] ,  tab['P11'] ,  tab['P12'] ]
resultat=pd . concat ( frames )

######Selecteur de calcul pour Energie HP de 6 H à 22 H, le reste en HC
selector_Calcul_EHP=(tab['P1'].index.hour>6) & (tab['P1'].index.hour<=22 ) & (tab['P1'].index.weekday<5)
selector_Calcul_EHC=(~selector_Calcul_EHP)