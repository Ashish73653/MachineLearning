# Problem with Python lists
import time
import numpy as np
SIZE = 1000000
# Create a Python list
py_list = list(range(SIZE))
# Measure time taken to compute the square of each element using a Python list
start_time = time.time()
py_list_squared = [x**2 for x in py_list]
end_time = time.time()
print("Time taken using Python list: {:.6f} seconds".format(end_time - start_time))
# Create a NumPy array
np_array = np.arange(SIZE)
# Measure time taken to compute the square of each element using a NumPy array
start_time = time.time()
np_array_squared = np_array ** 2
end_time = time.time()
print("Time taken using NumPy array: {:.6f} seconds".format(end_time -
  start_time))
# The NumPy array operation is significantly faster than the Python list operation.

size2=6
# problem with multiplying two lists
# Create two Python lists
list1 = list(range(size2))
list2 = list(range(size2))
# we cant do list1 * list2 directly
# we need to use a loop or list comprehension
# but with numpy we can do it directly
# Create two NumPy arrays
np_array1 = np.arange(size2)
np_array2 = np.arange(size2)
print(np_array1 * np_array2)  # Element-wise multiplication