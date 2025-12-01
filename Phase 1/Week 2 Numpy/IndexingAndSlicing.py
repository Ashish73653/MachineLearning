# Array Indexing and Slicing in NumPy
import numpy as np
# Create a 2D NumPy array
array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original 2D array:\n", array_2d)

# Accessing elements
element_1_2 = array_2d[1, 2]  # Access element at row 1, column 2
print("Element at (1, 2):", element_1_2)
element_0_0 = array_2d[0, 0]  # Access element at row 0, column 0
print("Element at (0, 0):", element_0_0)

# Slicing rows
first_row = array_2d[0, :]  # First row
print("First row:", first_row)
second_row = array_2d[1, :]  # Second row
print("Second row:", second_row)

# Slicing columns
first_column = array_2d[:, 0]  # First column
print("First column:", first_column)
second_column = array_2d[:, 1]  # Second column
print("Second column:", second_column)

# Slicing sub-arrays
sub_array = array_2d[0:2, 1:3]  # Rows 0-1, Columns 1-2
print("Sub-array (rows 0-1, columns 1-2):\n", sub_array)

# Modifying elements
array_2d[2, 2] = 100  # Change element at (2, 2) to 100
print("Modified array after changing element at (2, 2):\n", array_2d)
array_2d[0, :] = [1, 2, 3]  # Change first row
print("Modified array after changing first row:\n", array_2d)
array_2d[:, 1] = [9, 8, 7]  # Change second column
print("Modified array after changing second column:\n", array_2d)

# Boolean indexing
bool_index = array_2d > 50
print("Boolean index (elements > 50):\n", bool_index)
filtered_elements = array_2d[bool_index]
print("Filtered elements (elements > 50):", filtered_elements)

# Fancy indexing
row_indices = [0, 2]
col_indices = [1, 2]
fancy_indexed_elements = array_2d[row_indices, col_indices]
print("Fancy indexed elements (rows 0 & 2, columns 1 & 2):", fancy_indexed_elements)

# Combining indexing methods
combined_indexing = array_2d[1:, [0, 2]]  # Rows 1 to end, columns 0 and 2
print("Combined indexing (rows 1 to end, columns 0 and 2):\n", combined_indexing)

# Reshaping and then indexing 
reshaped_array = array_2d.reshape(1, 9)
print("Reshaped array (1x9):\n", reshaped_array)

# Accessing elements in reshaped array
element_0_4 = reshaped_array[0, 4]
print("Element at (0, 4) in reshaped array:", element_0_4)
element_0_7 = reshaped_array[0, 7]
print("Element at (0, 7) in reshaped array:", element_0_7)  

# Slicing in reshaped array
sliced_reshaped = reshaped_array[0, 2:5]
print("Sliced elements (2 to 4) in reshaped array:", sliced_reshaped)

# Modifying elements in reshaped array
reshaped_array[0, 5] = 999
print("Modified reshaped array after changing element at (0, 5):\n", reshaped_array)