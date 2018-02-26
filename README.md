# Desafio2 

###### Using Python3 version 3.5.2

##### Requirements to run desafio2 at requirements.txt

## File details
##### exportcontent.py 
Script to get content from The Guardian API and export to .csv file

##### content.py 
Class to get content from The Guardian API

## Configuration to testing
##### API Key 
To change value replace variable 'apikey' at file 'exportcontent.py'

##### Path to save the .csv file 
Default path is '/alice/desafio2/csv_files', to change value replace variable 'exportpath' at file 'exportcontent.py' 

## Steps to test
 - execute file exportcontent.py using 'from' and 'to' date required parameters on formart 'dd/mm/YYYY'
 - example: python3 exportcontent --from 01/01/2018 --to 10/01/2018

This example will search content by keyword 'education' from date '10/10/2018' to date '11/10/2018' and save content to file '/alice/desafio2/csv_files/content_f_10102018_t_10102018_$DatetimeOfExecution.csv'

**WARN: Some content may have escape characters that can cause csv misformatting**

