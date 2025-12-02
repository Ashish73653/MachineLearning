# Handling Missing Values in Pandas
import pandas as pd
import numpy as np
data = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
        'Age': [24, None, 22, 32, 29],
        'City': ['New York', 'Los Angeles', None, 'Houston', 'Phoenix']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Check for missing values
print("Check for missing values:")
print(df.isnull())
# Drop rows with any missing values
df_dropped = df.dropna()
print("DataFrame after dropping rows with missing values:")
print(df_dropped)
# Fill missing values with a specific value
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown'})
print("DataFrame after filling missing values:")
print(df_filled)
# Forward fill missing values
df_ffill = df.fillna(method='ffill')
print("DataFrame after forward filling missing values:")
print(df_ffill)
# Backward fill missing values
df_bfill = df.fillna(method='bfill')
print("DataFrame after backward filling missing values:")
print(df_bfill)
# Interpolate missing values in the 'Age' column
df_interpolated = df.copy()
df_interpolated['Age'] = df_interpolated['Age'].interpolate()
print("DataFrame after interpolating missing values in 'Age' column:")
print(df_interpolated)
# Replace missing values with a constant
df_replaced = df.replace(to_replace=np.nan, value='Missing')
print("DataFrame after replacing missing values with a constant:")
print(df_replaced)
# Check for not null values
print("Check for not null values:")
print(df.notnull())
# Count of missing values in each column
print("Count of missing values in each column:")
print(df.isnull().sum())
# Fill missing values using a custom function
print(df)
def fill_with_length(val):
    if pd.isnull(val):
        return 0
    else:
        return len(val)
df_custom_filled = df.copy()
df_custom_filled['Name'] = df_custom_filled['Name'].apply(fill_with_length)
print("DataFrame after filling 'Name' with length of string or 0 if missing:")  
print(df_custom_filled)
