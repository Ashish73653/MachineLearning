import numpy as np

# Creating a 1D array
a = np.array([1, 2, 3])
print("Array a:", a)
print("Type of a:", a.dtype)

# Creating a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Array b:\n", b)
print("Type of b:", b.dtype)

# Creating an array with a specific data type
c = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print("Array c with float type:\n", c)
print("Type of c:", c.dtype)

# print shape dimensions and total elements
print("Shape of a:", a.shape)
print("Dimensions of a:", a.ndim)
print("Total elements in a:", a.size)

print("Shape of b:", b.shape)
print("Dimensions of b:", b.ndim)
print("Total elements in b:", b.size)

print("Shape of c:", c.shape)
print("Dimensions of c:", c.ndim)
print("Total elements in c:", c.size)

# np.arrange function
d = np.arange(10)
print("Array d using np.arange(10):", d)
e = np.arange(5, 15)
print("Array e using np.arange(5, 15):", e)
f = np.arange(0, 20, 2)
print("Array f using np.arange(0, 20, 2):", f)

# np.linspace function
g = np.linspace(0, 1, 5)
print("Array g using np.linspace(0, 1, 5):", g)
h = np.linspace(10, 20, 4)
print("Array h using np.linspace(10, 20, 4):", h)
i = np.linspace(0, 100, 10)
print("Array i using np.linspace(0, 100, 10):", i)



# Plotting a sine wave using np.linspace
import numpy as np          # ✅ Needed for np.linspace and np.sin
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Create 100 equally spaced points between 0 and 2π
x = np.linspace(0, 2 * np.pi, 100)

# Compute sine of each x value
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)

# Add a title to the plot
plt.title("Sine Wave using np.linspace")

# Display the plot
plt.show()

"""
🧠 Explanation:
- np.linspace(0, 2π, 100) → generates 100 evenly spaced x-values from 0 to 2π.
- np.sin(x) → computes the sine for each of those x-values.
- plt.plot(x, y) → draws the sine curve.
- plt.show() → displays the plot window.

✅ Expected Output:
A smooth sine wave starting at (0,0), peaking at π/2, dipping at 3π/2, 
and returning to 0 at 2π.
"""


# Creating arrays of zeros, ones, random and empty values
zeros_array = np.zeros((2, 3))
print("Array of zeros:\n", zeros_array)
ones_array = np.ones((3, 2))
print("Array of ones:\n", ones_array)
random_array = np.random.rand(2, 2)
print("Array of random values:\n", random_array)
empty_array = np.empty((2, 2))
print("Array of empty values:\n", empty_array)

# Identity matrix
identity_matrix = np.eye(3)
print("Identity matrix:\n", identity_matrix)

# Diagonal matrix
diagonal_matrix = np.diag([1, 2, 3])
print("Diagonal matrix:\n", diagonal_matrix)

# Reshaping an array
reshaped_array = np.arange(6).reshape((2, 3))
print("Reshaped array:\n", reshaped_array)

# Flattening an array
flattened_array = reshaped_array.flatten()
print("Flattened array:\n", flattened_array)

# Transposing an array
transposed_array = reshaped_array.T
print("Transposed array:\n", transposed_array)

# Changing data type of an array
changed_type_array = reshaped_array.astype(float)
print("Array with changed data type:\n", changed_type_array)
print("Data type of changed_type_array:", changed_type_array.dtype)

# Copying an array
copied_array = reshaped_array.copy()
print("Copied array:\n", copied_array)

# Slicing an array
sliced_array = reshaped_array[:, 1:3]
print("Sliced array (columns 1 to 2):\n", sliced_array)

# Indexing an array
indexed_value = reshaped_array[1, 2]
print("Indexed value at (1,2):", indexed_value)

# Iterating over an array
for row in reshaped_array:
    print("Row:", row)

# Basic arithmetic operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("Array1 + Array2:", array1 + array2)
print("Array1 - Array2:", array1 - array2)
print("Array1 * Array2:", array1 * array2)
print("Array1 / Array2:", array1 / array2)
print("Array1 squared:", array1 ** 2)
print("Square root of Array2:", np.sqrt(array2))

# Statistical operations
print("Mean of array1:", np.mean(array1))
print("Median of array2:", np.median(array2))
print("Standard deviation of array1:", np.std(array1))
print("Sum of array2:", np.sum(array2))
print("Minimum of array1:", np.min(array1))
print("Maximum of array2:", np.max(array2))

# Dot product of two arrays
dot_product = np.dot(array1, array2)
print("Dot product of array1 and array2:", dot_product)

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.matmul(matrix1, matrix2)
print("Matrix product of matrix1 and matrix2:\n", matrix_product)

# Element-wise multiplication
elementwise_product = matrix1 * matrix2
print("Element-wise product of matrix1 and matrix2:\n", elementwise_product)

# Copy vs View
original_array = np.array([1, 2, 3, 4, 5])
copied_array = original_array.copy()
viewed_array = original_array.view()
viewed_array[0] = 10
print("Original array after modifying view:", original_array)
print("Copied array remains unchanged:", copied_array)
print("Viewed array after modification:", viewed_array)
print("Original array id:", id(original_array))
print("Copied array id:", id(copied_array))
print("Viewed array id:", id(viewed_array))
# The viewed_array shares the same data as original_array, so changes in viewed_array affect original_array.

# Broadcasting
array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([10, 20, 30])
broadcasted_sum = array3 + array4
print("Broadcasted sum:\n", broadcasted_sum)
# Here, array4 is broadcasted across the rows of array3 for addition.
