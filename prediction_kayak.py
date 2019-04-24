# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:34:32 2019

@author: Aspen
"""



from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pandas as pd 
import os

os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1\\git")

data=pd.read_csv("fixed_effects_data3.csv")
data=data.drop(['Unnamed: 0'], axis=1)
data_test=data[data['Price']!='Info']
data_pred=data[data['Price']=='Info']
data_test['Price']=data_test['Price'].str[1:].astype(int)
target=data_test.iloc[:,1]


######################## MODEL 1 

""" this includes only data on destinations """


M1=data_test.iloc[:,67:287]

regression1=linear_model.LinearRegression()  
regression1.fit(M1, target) 
results1 = regression1.predict(M1) 
r2_1=r2_score(target, results1) 
mse1=mean_squared_error(target, results1)

##############################  MODEL 2

""" This one includes both destinations and carriers"""

M2=data_test.iloc[:,31:287]
regression2=linear_model.LinearRegression()
regression2.fit(M2, target) 
results2 = regression2.predict(M2)
r2_2=r2_score(target, results2) 
mse2=mean_squared_error(target, results2) 

################################# MODEL 3 

""" This one includes destinations, carriers, and days of the week fixed effects""" 

M3=data_test.iloc[:,24:287]
regression3=linear_model.LinearRegression()
regression3.fit(M3, target) 
results3 = regression3.predict(M3)
r2_3=r2_score(target, results3) 
mse3=mean_squared_error(target, results3) 


###########################  MODEL 4 
""" This one inlcudes destinations, carriers, days of the week, and hour of the flight as a fixed effects"""
M4=data_test.iloc[:, 4:287]
regression4=linear_model.LinearRegression()
regression4.fit(M4, target) 
results4 = regression4.predict(M4)
r2_4=r2_score(target, results4) 
mse4=mean_squared_error(target, results4) 



#################### MODEL 5 
""" this one includes the destination, carrier, days of the week, and the number of stops """
cols = [3] + list(range(24,287))
M5= data_test.iloc[:,cols]
regression5=linear_model.LinearRegression()
regression5.fit(M5, target) 
results5 = regression5.predict(M5)
r2_5=r2_score(target, results5) 
mse5=mean_squared_error(target, results5) 


###################  MODEL 6 
""" this one includes the destination, carrier, days of the week, and the number of carriers """
cols = [0] + list(range(24,287))
M6= data_test.iloc[:,cols]
regression6=linear_model.LinearRegression()
regression6.fit(M6, target) 
results6 = regression6.predict(M6)
r2_6=r2_score(target, results6) 
mse6=mean_squared_error(target, results6) 


##################   Predicting Unkown Price 
M3_pred=data_pred.iloc[:,24:287]
results3_pred = pd.DataFrame(regression3.predict(M3_pred))
results3_pred.to_csv("results.csv")
