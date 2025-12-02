# Joins and Merges with Pandas
import pandas as pd
data1 = {'Key': ['A', 'B', 'C', 'D'],
         'Value1': [1, 2, 3, 4]}
data2 = {'Key': ['B', 'C', 'D', 'E'],
         'Value2': [5, 6, 7, 8]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("DataFrame 1:")
print(df1)
print("DataFrame 2:")
print(df2)
# Inner Join
inner_join = pd.merge(df1, df2, on='Key', how='inner')
print("Inner Join:")
print(inner_join)
# Left Join
left_join = pd.merge(df1, df2, on='Key', how='left')
print("Left Join:")
print(left_join)
# Right Join
right_join = pd.merge(df1, df2, on='Key', how='right')
print("Right Join:")
print(right_join)
# Outer Join
outer_join = pd.merge(df1, df2, on='Key', how='outer')
print("Outer Join:")
print(outer_join)
# Merging on multiple columns
data3 = {'Key1': ['A', 'B', 'C', 'D'],
          'Key2': [1, 2, 3, 4],
          'Value3': [10, 20, 30, 40]}
data4 = {'Key1': ['B', 'C', 'D', 'E'],
          'Key2': [2, 3, 4, 5],
          'Value4': [50, 60, 70, 80]}
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)
multi_merge = pd.merge(df3, df4, on=['Key1', 'Key2'], how='inner')
print("Merge on multiple columns:")
print(multi_merge)
# Concatenation
concat_df = pd.concat([df1, df2], ignore_index=True, sort=False)
print("Concatenation:")
print(concat_df)
# Appending (use concat; DataFrame.append is deprecated)
appended_df = pd.concat([df1, df2], ignore_index=True, sort=False)
print("Appending:")
print(appended_df)
# Joining using DataFrame.join()
data5 = {'Value5': [100, 200, 300, 400]}
df5 = pd.DataFrame(data5, index=['A', 'B', 'C', 'D'])
joined_df = df1.set_index('Key').join(df5, how='inner')
print("Joining using DataFrame.join():")
print(joined_df)