#  Reading CSV and JSON Files in Pandas
import pandas as pd
# Reading a CSV file
csv_file_path = 'data/sample_data.csv'  # Replace with your CSV file path
df_csv = pd.read_csv(csv_file_path)
print("DataFrame from CSV file:")
print(df_csv)
# Reading a JSON file
json_file_path = 'data/sample_data.json'  # Replace with your JSON file path
df_json = pd.read_json(json_file_path)
print("DataFrame from JSON file:")
print(df_json)
# Displaying first few rows of the DataFrames
print("First 5 rows of CSV DataFrame:")
print(df_csv.head())
print("First 5 rows of JSON DataFrame:")
print(df_json.head())
# Displaying summary statistics of the DataFrames
print("Summary statistics of CSV DataFrame:")
print(df_csv.describe())
print("Summary statistics of JSON DataFrame:")
print(df_json.describe())
# Displaying information about the DataFrames
print("Info of CSV DataFrame:")
print(df_csv.info())
print("Info of JSON DataFrame:")
print(df_json.info())
# Displaying column names of the DataFrames
print("Column names of CSV DataFrame:")
print(df_csv.columns)
print("Column names of JSON DataFrame:")
print(df_json.columns)
# Displaying data types of the columns in the DataFrames
print("Data types of CSV DataFrame:")
print(df_csv.dtypes)
print("Data types of JSON DataFrame:")
print(df_json.dtypes)