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



os.listdir()
for one_file_name in glob.glob("html_files/*.html"):
    print("parsing " + one_file_name)
scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
    file_name='ATL-SRQ_04-13.html'
    
    
f=open("ATL-SRQ_04-13.html", encoding="utf8")
soup=BeautifulSoup(f.read(), 'html.parser')    
f.close()

airline = soup.find_all('div', {'class':'resultInner'})
first=airline[1]

duration=first.find_all('div', {'class':'section duration'})
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
airline=upper[0].text
origin=upper[2].text[1:-7]
destination=upper[2].text[7:-1]





