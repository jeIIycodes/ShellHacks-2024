import pandas as pd
import numpy as np

#Plan of this file is to be able to read the two xlsx files and be able to work with the applicant data
#Make sure that the data is adequately preprocessed first
#For detail in data used, we will target the Detailed rows under O_GROUP if there is a duplicate

dfMay = pd.read_excel('data/MFF_EXPORT_2023_2024-01-17.xlsx', sheet_name=1)
dfNational = pd.read_excel('data/national_M2023_dl.xlsx')

print("First File: \n")
print(dfMay)
print("\n")
print("Second File: \n")
print(dfNational)

