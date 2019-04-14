# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:34:32 2019

@author: Aspen
"""



from sklearn.metrics import r2_score
import pandas as pd 
import os

os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1")

####################### REGULAR: STOPS, FIXED: DATE, HOUR, DESTINATION, AIRLINE    .910

data=pd.read_csv("clean_date.csv")

day=data.drop(['Unnamed: 0', 'Day'], axis=1)

day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']


day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,0]
day_test=day_test.drop(['Price'], axis=1)
day_pred=day_pred.drop(['Price'], axis=1)


regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 


################################## REGULAR: HOUR STOPS   FIXED EFFECTS: DATE, DEST, AIRLINE   .907

data=pd.read_csv("clean_no_hour.csv")

day=data.drop(['Unnamed: 0', 'Day'], axis=1)

day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']


day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,0]
day_test=day_test.drop(['Price'], axis=1)
day_pred=day_pred.drop(['Price'], axis=1)


regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 





################################## REGULAR: HOUR STOPS DATE,  FIXED EFFECTS: DATE, DEST, AIRLINE  R2   .907


###single day .9224 day=16
###single day .9224 day=17   0.9501
data=pd.read_csv("clean_no_hour.csv")

day=data.drop(['Unnamed: 0', 'Date_04-16', 'Date_04-17', 'Hour', 'Day', 'stops'], axis=1)
day=day[day['Day']==17]

day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']


day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,0]
day_test=day_test.drop(['Price'], axis=1)
day_pred=day_pred.drop(['Price'], axis=1)


regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 





################################## REGULAR: HOUR STOPS DATE,  FIXED EFFECTS: DATE, DEST, AIRLINE  R2   .907


###single day .9224 day=16
###single day .9224 day=17   0.9501
data=pd.read_csv("basic.csv")

day=data.drop(['Unnamed: 0','Hour', 'Day', 'stops', 'Date', ], axis=1)
day=day[day['Day']==17]

day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']


day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,0]
day_test=day_test.drop(['Price'], axis=1)
day_pred=day_pred.drop(['Price'], axis=1)


regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 


################################## REGULAR: HOUR STOPS DATE,  FIXED EFFECTS: DATE, DEST, AIRLINE  R2   .907


###single day .9224 day=16
###single day .9224 day=17   0.9501
data=pd.read_csv("basic.csv")

day=data.drop(['Unnamed: 0','Hour', 'Day', 'stops', 'Date', ], axis=1)
day=day[day['Day']==17]

day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']


day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,0]
day_test=day_test.drop(['Price'], axis=1)
day_pred=day_pred.drop(['Price'], axis=1)


regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 



################################## REGULAR: HOUR STOPS DATE,  FIXED EFFECTS: DATE, DEST, AIRLINE  R2   .907

data=pd.read_csv("dest_only.csv")

day=data.drop(['Unnamed: 0','Hour', 'Day', 'stops', 'Date', 'Carrier'], axis=1)
#day=day[day['Day']==17]

day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']


day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,0]
day_test=day_test.drop(['Price'], axis=1)
day_pred=day_pred.drop(['Price'], axis=1)


regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 


###############################

data=pd.read_csv("clean_no_hour.csv")
day=data.drop(['Unnamed: 0', 'Date_04-16', 'Date_04-17'], axis=1)


day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']


day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,2]
day_test=day_test.drop(['Hour'], axis=1)
#day_pred=day_pred.drop(['Price'], axis=1)


regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 















data=pd.read_csv("clean_hour.csv")

data=data[data['Day']==13]

day=data.drop(['Unnamed: 0'], axis=1)

day_test=day[day['Price']!='Info']
day_pred=day[day['Price']=='Info']
day_pred=day_pred[day_pred['Day']==13]

day_test['Price']=day_test['Price'].str[1:].astype(int)
target=day_test.iloc[:,0]
day_test=day_test.drop(['Price'], axis=1)
day_pred=day_pred.drop(['Price'], axis=1)




regression=linear_model.LinearRegression()
regression.fit(day_test, target) 
results = regression.predict(day_test)

r2_score(target, results) 




results2 = regression.predict(day_pred)





