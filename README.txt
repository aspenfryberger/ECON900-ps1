
This repository scrapes flight information from kayak.com, parses the data, and uses supervised machine learning to predict missing prices. 
This is done in 4 steps using 2 data files, 4 python files, and 1 driver file which exist in this repository. 

Step 1) 
a. Make sure you have the package Selenium installed. 

b. The geckodriver is required for the use of webdiver in Selenium, make sure it is in the specified path. This needs to match the path in line 27 of the "scrape_kayak.py" file. 

c. Use the "date.csv" and "codes.xls" as well as the geckodriver to run the python file "scrape_kayak.py". The date file gives the dates for which you would like to scrape
and the "codes.xls" file gives the airport codes for the destinations of the flight. Please note that both "data.csv" and "codes.xls" must be in the path for this code to work. 
All routes begin in Atlanta GA (This takes about 4 days). This code saves the html files outside the git hub repository due to file size issues with uploading them to github. If 
you would like to have the html files please contact me. 

Step 2) 
Use the "parse_kayak.py" code to parse the html files generated in the "scrape_kayak.py" code. This will generate the "data3.csv" file which is the fully parsed data. 
Again, this code pulls the html files that are kept outside the git repository. 

Step 3) 
Use the "data3.csv" file from step 2 and the "data_clearning.py" file to get the code ready for machine learning. This requires creating a dummy varibles for each categorical 
variable like destination, carrier, and day of the week. This code will create the cleaned file "fixed_effects_data3.csv". 

Step 4) 
Use the "fixed_effects_data3.csv" from setp 4 in the "prediction_kayak.py" code to run machine learning models on the data and predict the missing prices in the data. This 
generates the "results.csv" file which contains the predicted price for the flights with no price listed. The project summary file "Project_Summary.pdf" contains a write 
up of the project and an explanation of the data and machine learning. 

