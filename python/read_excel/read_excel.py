# example file taken from https://file-examples.com/index.php/sample-documents-download/sample-xls-download/

import pandas as pd
# read excel file
df = pd.read_excel('excelexample.xlsx')
#print head
print(df.head())
# change row 2, column 2
# change 'Philip' in 'John'
df.at[2,'First Name']='John'
# print head
print(df.head())
# write result to a new excel file
df.to_excel('excelexample_new.xlsx')


