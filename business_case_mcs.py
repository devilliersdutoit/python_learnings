# Import pandas
from pandas import ExcelFile
import numpy as np

# Assign spreadsheet filename to `file`
file: str = 'bc.xlsx'

# Load spreadsheet
xl = ExcelFile(file)

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

li: list = df1.values.tolist()

print(li)
# df2 = pd.DataFrame(li)
# print(df2)

# print(df1.equals(df2))
# df2.to_excel("output.xlsx")
# print(df1.loc[3].T)
# print(df1)
