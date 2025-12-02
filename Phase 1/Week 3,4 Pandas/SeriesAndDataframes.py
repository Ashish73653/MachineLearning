# Series
import pandas as pd
import numpy as np
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}
ser1 = pd.Series(my_data, index=labels)
ser2 = pd.Series(arr, labels)
ser3 = pd.Series(d)
print(ser1)
print(ser2)
print(ser3)
print(ser1['a'])
print(ser1.iloc[:1]) # slicing by position
print(ser1.loc['b']) # slicing by label
print(ser1.loc['a':'c']) # slicing by label inclusive
print(ser1 + ser2) # adding two series
print(ser1 + 5) # broadcasting
print(ser1.dtype) # data type
print(ser1.shape) # shape of series
print(ser1.index) # index of series
print(ser1.values) # values of series
print(ser1.isnull()) # check for null values
print(ser1.notnull()) # check for not null values
print(ser1.head(2)) # first n elements
print(ser1.tail(2)) # last n elements
print(ser1.sort_values()) # sort by values

# DataFrames
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)
print(df)
print(df['A']) # accessing a column
print(df.A) # accessing a column
print(df.loc[0]) # accessing a row by label
print(df.iloc[0]) # accessing a row by position 
print(df.loc[:, 'A']) # accessing all rows of column A
print(df.iloc[:, 0]) # accessing all rows of first column
print(df.describe()) # summary statistics
print(df.T) # transpose
print(df.sort_values(by='B')) # sort by column B
print(df.isnull()) # check for null values
print(df.notnull()) # check for not null values
print(df.head(2)) # first n rows  
print(df.tail(2)) # last n rows
print(df.shape) # shape of dataframe
print(df.dtypes) # data types of columns
print(df.columns) # column names
print(df.index) # index of dataframe
print(df.values) # values of dataframe
print(df.mean()) # mean of columns
print(df.sum()) # sum of columns

# Adding a new column
df['C'] = df['A'] + df['B']
print(df)
# Deleting a column
del df['C']
print(df)
# Adding a new row
new_row = pd.DataFrame({'A': [5], 'B': [9]})
df = pd.concat([df, new_row], ignore_index=True)
print(df)