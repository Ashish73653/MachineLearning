# Grouping and Aggregation with Pandas
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah'],
        'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
        'Salary': [50000, 60000, 55000, 52000, 70000, 72000, 58000, 51000],
        'Age': [25, 30, 28, 35, 40, 45, 32, 29]}
df = pd.DataFrame(data)
print(df)
# Group by Department and calculate mean Salary and Age
grouped = df.groupby('Department').agg({'Salary': 'mean', 'Age': 'mean'})
print(grouped)
# Group by Department and get the sum of Salary
salary_sum = df.groupby('Department').agg({'Salary': 'sum'})
# Or
# salary_sum = df.groupby('Department')['Salary'].sum()
print(salary_sum)
# Group by Department and get the maximum Age
max_age = df.groupby("Department").agg({"Age": "max"})
# Or
max_age_alt = df.groupby("Department")["Age"].max()
print(max_age)
print(max_age_alt)
# Group by multiple columns: Department and Age, and get the count of employees
grouped_multiple = df.groupby(['Department', 'Age']).size()
print(grouped_multiple)
# Resetting index after groupby
print(grouped)
reset_grouped = grouped.reset_index()
print(reset_grouped)
# Iterating through groups
for name, group in df.groupby('Department'):
    print(f"Department: {name}")
    print(group)
# Applying multiple aggregation functions
multi_agg = df.groupby('Department').agg({'Salary': ['mean', 'sum', 'max'], 'Age': ['min', 'max']})
print(multi_agg)
# Filtering groups based on a condition
filtered_groups = df.groupby('Department').filter(lambda x: x['Salary'].mean() > 55000)
print(filtered_groups)