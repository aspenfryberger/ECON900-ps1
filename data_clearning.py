# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:01:38 2019

@author: Aspen
"""

import pandas as pd 
from sklearn import linear_model
import os 
import numpy as np

os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1\\git")

data=pd.read_csv("data3.csv")

########getting rid of part samples 
#data=data[~(data['Carrier']=='Major Airline')|(data['Carrier']=='Multiple Airlines')]
data=data[~data['Depart_Time'].isnull()]

   

########Depart Time 
data[['hour', 'minute']]=data.Depart_Time.str.split(":",expand=True,).astype(int)
data['Hour']=np.where(data['Dep_meridiem']=='pm', data['hour']+12, data['hour'])
data['Hour_f']=data['Hour']

###########stops 
data['Flight_pattern']=data['Flight_pattern'].str[0:1]
data['stops']=np.where(data['Flight_pattern']=='n', '0', data['Flight_pattern']).astype(int)

###########Duration 
data[['d_hour', 'd_minute']]=data.Duration.str.split(" ",expand=True,)
data['d_hour']=data['d_hour'].str[:-1].astype(int)
data['d_minute']=data['d_minute'].str[:-1].astype(int)
data['Flight_time_minutes']=data['d_minute']+data['d_hour']*60


data2=data[['Hour_f', 'Price', 'Hour', 'stops', 'Date','Carrier', 'Destination', 'Flight_time_minutes']]

####### Carriers per route 
number=data.groupby(['Destination', 'Carrier']).agg({'Origin':'count'}).reset_index()
number2=number.groupby(['Destination']).agg({'Carrier':'count'}).reset_index()
number2.columns=['Destination', 'Num_carriers']


####### Flights per route 
number1=data.groupby(['Destination']).agg({'Origin':'count'}).reset_index()
number1.columns=['Destination', 'Num_flights']


data2=pd.merge(number2, data2, on='Destination', how='outer')
data2=pd.merge(number1, data2, on='Destination', how='outer')

data3=pd.get_dummies(data2, prefix=['Hour_f', 'Date', 'Carrier', 'Dest'],
                     columns=['Hour_f', 'Date',  'Carrier', 'Destination'])

data3.to_csv('fixed_effects_data3.csv')

##########descrtiptive stats

data_test=data2[data2['Price']!='Info']
data_pred=data2[data2['Price']=='Info']
data_test['Price']=data_test['Price'].str[1:].astype(int)

data_pred.to_csv('data2p.csv')
data_test.to_csv('data2t.csv')





