import pandas as pd
import numpy as np
upload = pd.read_csv('original/diabetic_data.csv') #upload dataset
print(upload)

upload = upload.replace('?', '999') #replace '?' values for NaN 

upload = upload.replace('NULL', '999') #replace 'NULL' values for 999

upload = upload.drop(columns=['payer_code'])

#Drop duplicates in the dataset 
upload.drop_duplicates()

#drop rows with missing values
#upload = upload.dropna()

#remove white spaces from values to prevent future inconvinience during analysis 
upload['diag_1'].str.strip()
upload['diag_2'].str.strip()
upload['diag_3'].str.strip()

#check column names in the dataset for reference 
upload.columns
upload.count
upload.loc[:,"weight"]

#Replace "No" for "0" for easier analysis 
upload.replace("No","0", inplace=True)
#Replace "None" for "0" for easier analysis 
upload.replace("None","0", inplace=True)
#Replace "Norm" to "1"
upload.replace("Norm","1", inplace=True)
#Replace "Yes" for 1 and "No" for "0" for easier analysis 
upload.replace(("Yes", "No"), ("1","0"), inplace=True)
#replace "No", "Steady", "Up", "Down" for "0", "2", "3", "4" 
upload.replace(("No", "Steady", "Up", "Down"), ("0", "2", "3", "4"), inplace=True)
#Replace "Ch" to "1" to indicate there was a change 
upload.replace(("Ch"), ("1"), inplace=True)
#Replace race column for number order AA= 1, C= 2, A= 3, O= 4
upload['race'].replace(("AfricanAmerican","Caucasian","Asian", 'Other'), ('1','2','3','4'), inplace=True)
#Replace gender column for number order Female= 1, Male= 2
upload['gender'].replace(('Female','Male'), ('1','2'), inplace=True)
#Replace age column 
upload['age'].replace(('[0-10)','[10-20)','[20-30)','[30-40)','[40-50)','[50-60)','[60-70)','[70-80)','[80-90)','[90-100)'), ('1','2','3','4','5','6','7','8','9','10'), inplace=True)
# [70-80)     305
# [60-70)     255
# [50-60)     177
# [80-90)     171
# [40-50)      68
# [30-40)      25
# [90-100)     22
# [20-30)      18
# [0-10)        1
# [10-20)       1

#Replace values in weight column
upload['weight'].replace(('[0-25)','[25-50)','[50-75)','[75-100)','[100-125)','[125-150)','[150-175)','[175-200)'),('1','2','3','4','5','6','7','8'), inplace=True)
# [75-100)     436
# [50-75)      286
# [100-125)    220
# [125-150)     46
# [25-50)       27
# [150-175)     16
# [175-200)      6
# [0-25) 

#Replace values in specialty column 
upload['medical_specialty'].replace(('Cardiology','InternalMedicine','Surgery-General','Family/GeneralPractice','ObstetricsandGynecology','Psychiatry','Pediatrics','Dentistry'),('1','2','3','4','5','6','7','8'), inplace=True)

#Cardiology                374
# InternalMedicine           295
# Surgery-General            255
# Family/GeneralPractice      81
# ObstetricsandGynecology     24
# Psychiatry                  11
# Pediatrics                   2
# Dentistry  

#Check for data types
upload.dtypes 

###########################################
#### IDENTIFY VALUES IN EACH COLUMN FOR ###
########## DATA DICTIONARY ################
###########################################

upload['encounter_id'].value_counts() #Unique identifiers
upload['patient_nbr'].value_counts() #Unique identifiers
upload['race'].value_counts() #race
upload['gender'].value_counts() 
upload['age'].value_counts() #age ranges
upload['weight'].value_counts() #Unique identifiers
upload['admission_type_id'].value_counts() #Unique identifiers
upload['discharge_disposition_id'].value_counts()
upload['admission_source_id'].value_counts()
upload['time_in_hospital'].value_counts()
upload['medical_specialty'].value_counts() 
# #Cardiology                374
# InternalMedicine           295
# Surgery-General            255
# Family/GeneralPractice      81
# ObstetricsandGynecology     24
# Psychiatry                  11
# Pediatrics                   2
# Dentistry                    1

upload['num_lab_procedures'].value_counts()
upload['num_lab_procedures'].max()
upload['num_lab_procedures'].min()

upload['num_procedures'].value_counts()
upload['num_procedures'].max()
upload['num_procedures'].min()

upload['num_medications'].value_counts()
upload['num_medications'].max()
upload['num_medications'].min()

upload['number_outpatient'].value_counts()
upload['number_outpatient'].max()
upload['number_outpatient'].min()



upload['number_emergency'].value_counts()
upload['number_emergency'].max()
upload['number_emergency'].min()


upload['number_inpatient'].value_counts()

upload['diag_1'].value_counts()
upload['diag_1'].max()
upload['diag_1'].min()

upload['diag_2'].value_counts()
upload['diag_2'].max()
upload['diag_2'].min()



upload['diag_3'].value_counts()
upload['diag_3'].max()
upload['diag_3'].min()


upload['number_diagnoses'].value_counts()
upload['number_diagnoses'].max()
upload['number_diagnoses'].min()

upload['max_glu_serum'].value_counts() #None
upload['A1Cresult'].value_counts() #None, >8, >7, Norm
upload['metformin'].value_counts() #No, Steady, Up, Down 
upload['repaglinide'].value_counts() #No, Steady, Up 
upload['nateglinide'].value_counts() #NO, Steady
upload['chlorpropamide'].value_counts() #NO 
upload['glimepiride'].value_counts() #No, Steady, Up, Down 
upload['acetohexamide'].value_counts() #NO 
upload['glipizide'].value_counts() #No, Steady, Up, Down 
upload['glyburide'].value_counts() #No, Steady, Up, Down 
upload['tolbutamide'].value_counts() #NO
upload['pioglitazone'].value_counts() #No, Steady, Up, Down 
upload['rosiglitazone'].value_counts() #No, Steady
upload['acarbose'].value_counts() #No, Steady
upload['miglitol'].value_counts() #NO 
upload['troglitazone'].value_counts() #NO 
upload['tolazamide'].value_counts() #NO 
upload['examide'].value_counts() #NO 
upload['citoglipton'].value_counts() #NO 
upload['insulin'].value_counts() #No, Steady, Up, Down 
upload['glyburide-metformin'].value_counts() #NO
upload['glipizide-metformin'].value_counts() #NO
upload['glimepiride-pioglitazone'].value_counts() #NO
upload['metformin-rosiglitazone'].value_counts() #NO
upload['metformin-pioglitazone'].value_counts() #NO
upload['change'].value_counts() #No, Ch
upload['diabetesMed'].value_counts() #Yes, No
upload['readmitted'].value_counts() #>30, NO, <30 

upload.to_csv('original/clean_data.csv', index=False)