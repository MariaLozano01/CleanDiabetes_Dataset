import pandas as pd
import numpy as np
upload = pd.read_csv('original/diabetic_data.csv', na_values = '?') #replace '?' values for NaN
print(upload)

#drop rows with missing values
upload = upload.dropna()
upload

upload.columns #check columns in the dataset for refeerence 
upload.loc[:,"weight"]
upload


countRows, countColumns = upload.shape #This line assigns names to each value
countRows #Ran it to be able to see the number of rows in our dataset
countColumns #Ran it to be able to see the number of columns in our dataset

#Change data types to correct ones 
#
#Step 3 provides column names
list(upload)
#Step 4 cleans column names
upload.columns = upload.columns.str.replace('[^A-Za-z0-9]+', '_')
#Step 5 cleans the strings that might exist within each column
strings = upload.select_dtypes(include=['object']).columns
strings
#Step 6 Assesses white space or special characters 
list(upload) #White spaces were replaced by an underscore when line 13 was ran
#Step 7 Converts the column types to the correct types 
numbers = upload.select_dtypes(include=['int64', 'float64']).columns
numbers
booleans = upload.select_dtypes(include=['bool']).columns
booleans

#rows with with missing values 
upload = upload.dropna()

upload.dtypes 

#Step 8 Look for duplicate rows and remove any duplicate rows

print(upload.duplicated()) #this line is to see which columns have suplicates
print(upload.duplicated().sum()) #This line is to define how many duplicates there are

#The record has no duplicates to remove 

#Step 9 count of missing values per column
upload.isnull().sum() 

#Step 10 #This line was added to make a new column named "Modality in Person" and determines whether to assign a 'True' statement if the row was "In PEerson" or 'False' statement if otherwise
upload['modality_inperson'] = pd.np.where(upload.Learning_Modality.str.contains('In Person'), 'true', 'false')
print(upload.head()) #this lines was done to view the entire table and make sure the modality column was added 


