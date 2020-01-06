# Import pandas
import pandas as pd
import numpy as np

# Assign spreadsheet filename to `file`
file = 'bc.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
# print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse(xl.sheet_names[1])
# print(df1.shape[0])
# print(df1.shape[1])
# print(df1)

# datafram to dictionary
# print(df1.to_dict('list'))

# datafram to list
li = df1.values.tolist()
print(li)
df2 = pd.DataFrame(li)
print(df2)

print(df1.equals(df2))

# print(df1.loc[3].T)
# print(df1)
