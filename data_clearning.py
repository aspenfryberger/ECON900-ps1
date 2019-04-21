# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:01:38 2019

@author: Aspen
"""

import pandas as pd 
from sklearn import linear_model
import os 
import numpy as np

os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1")

data=pd.read_csv("data3.csv")

########getting rid of part samples 
#data=data[~(data['Carrier']=='Major Airline')|(data['Carrier']=='Multiple Airlines')]
data=data[~data['Depart_Time'].isnull()]

   

########Depart Time 
data[['hour', 'minute']]=data.Depart_Time.str.split(":",expand=True,).astype(int)
data['Hour']=np.where(data['Dep_meridiem']=='pm', data['hour']+12, data['hour'])

###########stops 
data['Flight_pattern']=data['Flight_pattern'].str[0:1]
data['stops']=np.where(data['Flight_pattern']=='n', '0', data['Flight_pattern']).astype(int)

###########Duration 
data[['d_hour', 'd_minute']]=data.Duration.str.split(" ",expand=True,)
data['d_hour']=data['d_hour'].str[:-1].astype(int)
data['d_minute']=data['d_minute'].str[:-1].astype(int)
data['Flight_time_minutes']=data['d_minute']+data['d_hour']*60
data['Hour_f']=data['Hour']

data2=data[['Hour_f', 'Price', 'Hour', 'stops', 'Date','Carrier', 'Destination']]

####### Carriers per route 
number=data.groupby(['Destination', 'Carrier']).agg({'Origin':'count'}).reset_index()
number2=number.groupby(['Destination']).agg({'Carrier':'count'}).reset_index()
number2.columns=['Destination', 'Num_carriers']

data2=pd.merge(number2, data2, on='Destination', how='outer')


data3=pd.get_dummies(data2, prefix=['Hour_f', 'Date', 'Carrier', 'Dest'],
                     columns=['Hour_f', 'Date',  'Carrier', 'Destination'])

data3.to_csv('fixed_effects_data2.csv')









################################################## Other 

data4=pd.get_dummies(data2, prefix=['Date', 'Dest', 'Carrier'], 
                     columns=['Date', 'Destination', 'Carrier'])

data5=pd.get_dummies(data2, prefix=['Dest', 'Carrier'], 
                     columns=['Destination', 'Carrier'])

data6=pd.get_dummies(data2, prefix=['Dest'], 
                     columns=['Destination'])


data7=data[['Price', 'Hour', 'stops', 'Destination', 'Carrier']]

data7=data7[data7['Price']=='Info']

data7['Price']=data7['Price'].str[1:].astype(int)

a=data7.describe()

print(data7.describe().as_latex())

data8=data7.groupby(['Destination', 'Carrier']).agg({'Price':'count'}).reset_index()
data8=data8.groupby(['Destination']).agg({'Carrier':'count'})
data8.describe()
#data3=data[['Price', 'Destination', 'Day', 'Hour', 'stops', 'Carrier']]
#data3=pd.get_dummies(data3, prefix=['Dest', 'Carrier', 'Hour'], 
 #                    columns=['Destination', 'Carrier', 'Hour'])
 data.to_csv("for_r.csv")
 
 
data7.to_csv("for_r.csv")
data3.to_csv("clean_date.csv")
data4.to_csv("clean_no_hour.csv")
data5.to_csv("basic.csv")
data6.to_csv("dest_only.csv")

