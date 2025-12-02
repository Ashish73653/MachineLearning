# Filtering
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
df = pd.DataFrame(data)
print(df)
# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print(filtered_df)
# Filter rows where City is 'Chicago'
filtered_df2 = df[df['City'] == 'Chicago']
print(filtered_df2)

# Slicing
# Slicing rows by position
sliced_df = df.iloc[1:4]  # rows from index 1 to 3
print(sliced_df)
# Slicing rows by label
sliced_df2 = df.loc[1:3]  # rows from index 1 to 3
print(sliced_df2)
# Slicing specific columns
sliced_df3 = df.loc[:, ['Name', 'City']]  # all rows,
print(sliced_df3) # specific columns
# Slicing both rows and columns
sliced_df4 = df.loc[1:3, ['Name', 'City']]  # rows from index 1 to 3, specific columns
print(sliced_df4)
# Conditional slicing
sliced_df5 = df[(df['Age'] > 25) & (df['City'] == 'Los Angeles')]
print(sliced_df5)
# Using .query() method for filtering
sliced_df6 = df.query('Age > 25 and City == "Los Angeles"')
print(sliced_df6)
# Using .isin() method for filtering
sliced_df7 = df[df['City'].isin(['Chicago', 'Houston'])]
print(sliced_df7)
# Resetting index after filtering
reset_df = filtered_df.reset_index(drop=True)
print(reset_df)
# Setting a new index
set_index_df = df.set_index('Name')
print(set_index_df)
# Accessing rows using the new index
accessed_row = set_index_df.loc['Alice']
print(accessed_row)
# Resetting index back to default
default_index_df = set_index_df.reset_index()
print(default_index_df)
# Adding a new column based on conditions
df['Senior'] = df['Age'] > 28
print(df)
# Dropping a column
df_dropped = df.drop('Senior', axis=1)
print(df_dropped) 
# Dropping rows with missing values
data_with_nan = {'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
                 'Age': [24, None, 22, 32, 29],
                  'City': ['New York', 'Los Angeles', None, 'Houston', 'Phoenix']}
df_with_nan = pd.DataFrame(data_with_nan)
print(df_with_nan)
df_dropped_nan = df_with_nan.dropna()
print(df_dropped_nan)
# Filling missing values
df_filled_nan = df_with_nan.fillna({'Name': 'Unknown', 'Age': df_with_nan['Age'].mean(), 'City': 'Unknown'})
print(df_filled_nan)