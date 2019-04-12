# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:01:38 2019

@author: Aspen
"""

import pandas as pd 
from sklearn import linear_model
import os 

os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1")


test=data.groupby(['Destination', 'Date']).agg({'Price':'count'}).reset_index()
test2=test.groupby('Date').agg({'Destination':'count'})

data=pd.read_csv("data.csv")
data=data[~(data['Carrier']=='Major Airline')|(data['Carrier']=='Multiple Airlines')]
Major Airline
data['Carrier'].unique()
data[']


price_data=data[data['Price']!='Info']
test_data=data[data['Price']=='Info']

price_data['Price']=price_data['Price'].str[1:].astype(int)
price_data['Day']=price_data['Date'].str[3:].astype(int)
price_data[['hour', 'minute']]=price_data.Depart_Time.str.split(":",expand=True,).astype(int)


price_data['Hour']=np.where(price_data['Dep_meridiem']=='pm', price_data['hour']+12, price_data['hour'])
price_data['Flight_pattern']=price_data['Flight_pattern'].str[0:1]
price_data['stops']=np.where(price_data['Flight_pattern']=='n', '0', price_data['Flight_pattern']).astype(int)


price_data['Destination']=price_data['Destination'].astype('category')


target=price_data.iloc[:,5]
data=price_data[['Destination', 'stops', 'Hour']]
data=data.iloc[:, ].values


regression=linear_model.LinearRegression()

regression.fit(data, target) 

