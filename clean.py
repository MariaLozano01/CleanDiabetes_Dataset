import pandas as pd
import numpy as np
upload = pd.read_csv('original/diabetic_data.csv') #upload dataset
print(upload)

upload = upload.replace("?", np.nan)  #replace '?' values for NaN
print(upload)
upload["weight"]

upload.drop_duplicates() #drop duplicates in the dataset 

#drop rows with missing values
upload = upload.dropna()

#remove white spaces from values to prevent future inconvinience during analysis 
upload['diag_1'].str.strip()
upload['diag_2'].str.strip()
upload['diag_3'].str.strip()

#check column names in the dataset for reference 
upload.columns 
upload.count
upload.loc[:,"weight"]

#########################################
### Change data types to correct ones ###
#########################################

upload.dtypes 


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


#Step 9 count of missing values per column
upload.isnull().sum() 

#Step 10 #This line was added to make a new column named "Modality in Person" and determines whether to assign a 'True' statement if the row was "In PEerson" or 'False' statement if otherwise
upload['modality_inperson'] = pd.np.where(upload.Learning_Modality.str.contains('In Person'), 'true', 'false')
print(upload.head()) #this lines was done to view the entire table and make sure the modality column was added 


