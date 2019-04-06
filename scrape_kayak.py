# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:34:45 2019

@author: Aspen
"""

import selenium   #not sure if I need this 
from selenium import webdriver
import os
import pandas as pd

os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1")
codes=pd.read_excel("codes.xlsx")

codes=codes['name'].str.split(",", expand=True)
codes.columns=['one', 'two', 'three']
names=codes[['one']]
codes=codes['two'].str.split(" ", expand=True)
codes.columns=['one', 'two', 'three', 'other', 'other2', 'others', 'other4']
codes['three']=codes['three'].str[1:4]
code2=codes[['three']
codes3=names.join(code2)
codes3=codes3.astype(str)
codes3.to_csv('airport_codes.csv')

#############

code=pd.read_excel("codes.xlsx")
driver = webdriver.Firefox(executable_path = 'C:/Users/Aspen/Documents/EV/code/EV_scrape/geckodriver')
i=5
a=code.iloc[i, 1]
driver.get('https://www.kayak.com/flights/ATL-'+a+'/2019-04-05/2019-05-07?sort=bestflight_a')
#driver.get('https://www.kayak.com/flights/ATL-DEN/2019-04-05/2019-05-07?sort=bestflight_a')
html = driver.page_source

f=open("test.html","w", encoding='utf8')
f.write(html)
f.close() 












############################
f = open("test.html", "r")










