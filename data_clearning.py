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

data=pd.read_csv("data2.csv")
#data=data[~(data['Carrier']=='Major Airline')|(data['Carrier']=='Multiple Airlines')]


data['Day']=data['Date'].str[3:].astype(int)
data[['hour', 'minute']]=data.Depart_Time.str.split(":",expand=True,).astype(int)
data['Hour']=np.where(data['Dep_meridiem']=='pm', data['hour']+12, data['hour'])
data['Flight_pattern']=data['Flight_pattern'].str[0:1]
data['stops']=np.where(data['Flight_pattern']=='n', '0', data['Flight_pattern']).astype(int)
data2=data[['Price', 'Destination', 'Day', 'Date', 'Hour', 'stops', 'Carrier']]
data3=pd.get_dummies(data2, prefix=['Date', 'Hour', 'Dest', 'Carrier'], 
                     columns=['Date', 'Hour', 'Destination', 'Carrier'])

data4=pd.get_dummies(data2, prefix=['Date', 'Dest', 'Carrier'], 
                     columns=['Date', 'Destination', 'Carrier'])

data5=pd.get_dummies(data2, prefix=['Dest', 'Carrier'], 
                     columns=['Destination', 'Carrier'])

data6=pd.get_dummies(data2, prefix=['Dest'], 
                     columns=['Destination'])


#data3=data[['Price', 'Destination', 'Day', 'Hour', 'stops', 'Carrier']]
#data3=pd.get_dummies(data3, prefix=['Dest', 'Carrier', 'Hour'], 
 #                    columns=['Destination', 'Carrier', 'Hour'])

data3.to_csv("clean_date.csv")
data4.to_csv("clean_no_hour.csv")
data5.to_csv("basic.csv")
data6.to_csv("dest_only.csv")

