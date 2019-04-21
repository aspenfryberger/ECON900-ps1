# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:34:45 2019

@author: Aspen
"""
import time
import selenium   #not sure if I need this 
from selenium import webdriver
import os
import pandas as pd
from random import*
from sklearn.utils import shuffle

start_time = time.time()
os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1")

code=pd.read_excel("codes.xlsx")  #this has airport codes
date=pd.read_csv("date.csv")  #this is a data frame of dates
date['month']=date['month'].map("{:02}".format)
date['day']=date['day'].map("{:02}".format)
code=shuffle(code).reset_index()
code=code.drop(["index"], axis=1) 
date=shuffle(date).reset_index()
date=date.drop(["index"], axis=1)
os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1\\files")
driver = webdriver.Firefox(executable_path = 'C:/Users/Aspen/Documents/EV/code/EV_scrape/geckodriver')

for i in range(0,len(code)):
        c=code.iloc[i, 1]
        r=randint(1, 10)
        time.sleep(3+r)
        for j in range(0,len(date)):
            a=date.iloc[j,0]
            b=date.iloc[j,1]
            r=randint(1, 15)
            time.sleep(2+r)
            driver.get('https://www.kayak.com/flights/ATL-'+c+'/2019-'+a+'-'+b+'?sort=bestflight_a')
            time.sleep(30+r)
            html = driver.page_source
            f=open("ATL-"+c+"_"+a+"-"+b+".html","w", encoding='utf8')
            f.write(html)
            f.close() 
            r=randint(1, 80)
            time.sleep(50+r)
    
driver.close()   
print("--- %s seconds ---" % (time.time() - start_time))











