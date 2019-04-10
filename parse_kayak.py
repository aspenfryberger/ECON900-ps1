# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:51:21 2019

@author: Aspen
"""


from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
os.chdir("C:\\Users\\Aspen\\Documents\\Toms class\\project_1\\files")


for one_file_name in glob.glob("html_files/*.html"):
    
df=pd.DataFrame(columns=['Origin','Destination','Carrier','Price','Depart_Time','Dep_meridiem',
                              'Arrive_time','Arrival_time_meridiem', 'Flight_pattern'])
        
       
    f=open("filename", encoding="utf8")
    soup=BeautifulSoup(f.read(), 'html.parser')    
    f.close()
    airline = soup.find_all('div', {'class':'resultInner'})
    #airline = soup.find_all('div', {'class':'resultWrapper'})
    
    for i in range(0,len(airline)):
        first=airline[i]
        
        #duration=first.find_all('div', {'class':'section duration'})
        top=first.find_all('div', {'class':'top'})
        two=top[0]
        depart_time= two.find('span', {'class':'depart-time base-time'}).text[0:-1]
        meridiem = two.find_all('span', {'class':'time-meridiem meridiem'})
        departure_time_meridiem=meridiem[0].text
        arrival_time_meridiem=meridiem[1].text
        arrive_time=two.find('span', {'class':'arrival-time base-time'}).text[0:-1]
        flight_pattern=duration2[1].text[1:-1]
        
        duration=duration2[2].text
        upper=first.find_all('div', {'class':'bottom'})
        carrier=upper[0].text
        origin=upper[2].text[1:-7]
        destination=upper[2].text[7:-1]
        price=first.find('span', {'class':'price option-text'}).text[1:-1]
        
        
        df = df.append({
			'Origin': origin, 
			'Destination':destination,
			'Carrier': carrier,
			'Price': price,
			'Depart_Time': depart_time,
			'Dep_meridiem': departure_time_meridiem,
			'Arrive_time': arrive_time,
			'Arrival_time_meridiem': arrival_time_meridiem
            #'Flight_pattern': arrival_time_meridiem
			}, ignore_index=True)

df.to_csv('data.csv')

