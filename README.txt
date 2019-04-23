
This repository scrapes flight information from kayak.com, parses the data, and uses supervised machine learning to predict missing prices. 
This is done in 4 steps using 2 data files, 4 python files, and 1 driver file which exist in this repository. 

Step 1) 
a. Make sure you have the package Selenium installed. 

b. The geckodriver is required for the use of webdiver in Selenium, make sure it is in the specified path. 

c. Use the "date.csv" and "codes.xls" as well as the geckodriver to run the python file "scrape_kayak.py". The date file gives the dates for which you would like to scrape
and the "codes.xls" file gives the airport codes for the destinations of the flight. All routes begin in Atlanta GA. (This takes about 4 days)

Step 2) 
Use the "parse_kayak.py" code to parse the html files generated in the "scrape_kayak.py" code. This will generate the "data3.csv" file. 

Step 3) 
Use the "data2.csv" file and the "data_clearning.py" file get the code ready to run for machine learning. This requires creating dummy varibles for categorical variables 
like destination, and carrier. This will create the cleaned file "fixed_effects_data3.csv". 

Step 4) 
Use the "fixed_effects_data3.csv" in the "prediction_kayak.py" code to run machine learning models on the data and predict the missing price in the data. This generates the 
"results.csv" file which contains the predicted price for the flights with no price listed. 