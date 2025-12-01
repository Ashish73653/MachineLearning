# Element wise Operations in Numpy
import numpy as np
# Create two 1D arrays (vectors)
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
# Element-wise addition
c = a + b
print("Element-wise addition:\n", c)
# Output:
# Element-wise addition:
# [11 22 33 44]
# Element-wise subtraction
d = b - a
print("Element-wise subtraction:\n", d)
# Output:
# Element-wise subtraction:
# [9 18 27 36]  
# Element-wise multiplication
e = a * b
print("Element-wise multiplication:\n", e)
# Output:
# Element-wise multiplication:
# [10 40 90 160]
# Element-wise division
f = b / a
print("Element-wise division:\n", f)
# Output:
# Element-wise division:
# [10. 10. 10. 10.]
# Element-wise exponentiation
g = a ** 2
print("Element-wise exponentiation:\n", g)
# Output:
# Element-wise exponentiation:
# [ 1  4  9 16]
# Element-wise square root
h = np.sqrt(b)
print("Element-wise square root:\n", h)
# Output:
# Element-wise square root:
# [3.16227766 4.47213595 5.47722558 6.32455532]
# Element-wise logarithm
i = np.log(b)
print("Element-wise logarithm:\n", i)
# Output:
# Element-wise logarithm:
# [2.30258509 2.99573227 3.40119738 3.68887945]


# Universal functions (ufuncs) in NumPy
# Using np.sin on an array
j = np.array([0, np.pi/2, np.pi, 3*np.pi/2])
sin_j = np.sin(j)
print("Element-wise sine:\n", sin_j)
# Output:
# Element-wise sine:
# [ 0.  1.  0. -1.]
# Using np.exp on an array
k = np.array([0, 1, 2, 3])
exp_k = np.exp(k)
print("Element-wise exponential:\n", exp_k)
# Output:
# Element-wise exponential:
# [ 1.  2.71828183  7.3890561  20.08553692]
# Using np.maximum on two arrays
l = np.array([1, 4, 3, 8])
m = np.array([2, 3, 5, 7])
max_lm = np.maximum(l, m)
print("Element-wise maximum:\n", max_lm)
# Output:
# Element-wise maximum:
# [2 4 5 8]
# Using np.minimum on two arrays
min_lm = np.minimum(l, m)
print("Element-wise minimum:\n", min_lm)
# Output:
# Element-wise minimum:
# [1 3 3 7]
# Using np.abs on an array
n = np.array([-1, -2, 3, -4])
abs_n = np.abs(n)
print("Element-wise absolute value:\n", abs_n)
# Output:
# Element-wise absolute value:
# [1 2 3 4]
# Using np.mod on two arrays
o = np.array([10, 20, 30, 40])
p = np.array([3, 7, 4, 6])
mod_op = np.mod(o, p)
print("Element-wise modulus:\n", mod_op)
# Output:
# Element-wise modulus:
# [1 6 2 4]
# Using np.floor on an array
q = np.array([1.5, 2.3, 3.7, 4.9])
floor_q = np.floor(q)
print("Element-wise floor:\n", floor_q)
# Output:
# Element-wise floor:
# [1. 2. 3. 4.]
# Using np.ceil on an array
ceil_q = np.ceil(q)
print("Element-wise ceiling:\n", ceil_q)
# Output:
# Element-wise ceiling:
# [2. 3. 4. 5.]
# Using np.round on an array
round_q = np.round(q)
print("Element-wise round:\n", round_q)
# Output:
# Element-wise round:
# [2. 2. 4. 5.]
# Using np.sign on an array
sign_n = np.sign(n)
print("Element-wise sign:\n", sign_n)
# Output:
# Element-wise sign:
# [-1 -1  1 -1]
# Using np.clip on an array
clip_q = np.clip(q, 2, 4)
print("Element-wise clip:\n", clip_q)
# Output:
# Element-wise clip:
# [2. 2. 3. 4.]
# Using np.cumsum on an array
cumsum_a = np.cumsum(a)
print("Element-wise cumulative sum:\n", cumsum_a)
# Output:
# Element-wise cumulative sum:
# [ 1  3  6 10]
# Using np.cumprod on an array
cumprod_a = np.cumprod(a)
print("Element-wise cumulative product:\n", cumprod_a)
# Output:
# Element-wise cumulative product:
# [ 1  2  6 24]
# Using np.diff on an array
diff_b = np.diff(b)
print("Element-wise difference:\n", diff_b)
# Output:
# Element-wise difference:
# [10 10 10]


# Aggregation functions in NumPy
# Using np.sum on an array
sum_a = np.sum(a)
print("Sum of array a:\n", sum_a)
# Output:
# Sum of array a:
# 10
# Using np.mean on an array
mean_b = np.mean(b)
print("Mean of array b:\n", mean_b)
# Output:
# Mean of array b:
# 25.0
# Using np.std on an array
std_b = np.std(b)
print("Standard deviation of array b:\n", std_b)
# Output:
# Standard deviation of array b:
# 12.909944487358056
# Using np.var on an array
var_b = np.var(b)
print("Variance of array b:\n", var_b)
# Output:
# Variance of array b:
# 166.66666666666666
# Using np.min on an array
min_a = np.min(a)
print("Minimum of array a:\n", min_a)
# Output:
# Minimum of array a:
# 1
# Using np.max on an array
max_b = np.max(b)
print("Maximum of array b:\n", max_b)
# Output:
# Maximum of array b:
# 40
# Using np.argmin on an array
argmin_a = np.argmin(a)
print("Index of minimum of array a:\n", argmin_a)
# Output:
# Index of minimum of array a:
# 0
# Using np.argmax on an array
argmax_b = np.argmax(b)
print("Index of maximum of array b:\n", argmax_b)
# Output:
# Index of maximum of array b:
# 3
# Using np.median on an array
median_b = np.median(b)
print("Median of array b:\n", median_b)
# Output:
# Median of array b:
# 25.0
# Using np.prod on an array
prod_a = np.prod(a)
print("Product of array a:\n", prod_a)
# Output:
# Product of array a:
# 24
# Using np.all on an array
all_positive = np.all(a > 0)
print("Are all elements in array a positive?\n", all_positive)
# Output:
# Are all elements in array a positive?
# True
# Using np.any on an array
any_greater_than_three = np.any(a > 3)
print("Is any element in array a greater than 3?\n", any_greater_than_three)
# Output:
# Is any element in array a greater than 3?
# True
# Using np.unique on an array
r = np.array([1, 2, 2, 3, 4, 4, 4])
unique_r = np.unique(r)
print("Unique elements in array r:\n", unique_r)
# Output:
# Unique elements in array r:
# [1 2 3 4]
# Using np.sort on an array
unsorted_array = np.array([3, 1, 4, 2])
sorted_array = np.sort(unsorted_array)
print("Sorted array:\n", sorted_array)
# Output:
# Sorted array:
# [1 2 3 4]


# Axis based operations in NumPy
# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Sum along columns (axis=0)
sum_columns = np.sum(matrix, axis=0)
print("Sum along columns:\n", sum_columns)
# Output:
# Sum along columns:
# [12 15 18]
# Sum along rows (axis=1)
sum_rows = np.sum(matrix, axis=1)
print("Sum along rows:\n", sum_rows)
# Output:
# Sum along rows:
# [ 6 15 24]
# Mean along columns (axis=0)
mean_columns = np.mean(matrix, axis=0)
print("Mean along columns:\n", mean_columns)
# Output:
# Mean along columns:
# [4. 5. 6.]
# Mean along rows (axis=1)
mean_rows = np.mean(matrix, axis=1)
print("Mean along rows:\n", mean_rows)
# Output:
# Mean along rows:
# [2. 5. 8.]
# Standard deviation along columns (axis=0)
std_columns = np.std(matrix, axis=0)
print("Standard deviation along columns:\n", std_columns)
# Output:
# Standard deviation along columns:
# [2.44948974 2.44948974 2.44948974]


# Practical example: Normalizing data
data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# Normalize each column (feature) to have mean 0 and std 1
mean_data = np.mean(data, axis=0)
std_data = np.std(data, axis=0)
normalized_data = (data - mean_data) / std_data
print("Normalized data:\n", normalized_data)
# Output:
# Normalized data:
# [[-1.22474487 -1.22474487 -1.22474487]
#  [ 0.          0.          0.        ]
#  [ 1.22474487  1.22474487  1.22474487]]
# Note: Element-wise operations are fundamental in NumPy and are optimized for performance, allowing for efficient computations on large datasets.

# Practical example: Applying a threshold
thresholded_data = np.where(data > 50, 1, 0)
print("Thresholded data (1 if > 50 else 0):\n", thresholded_data)
# Output:
# Thresholded data (1 if > 50 else 0):
# [[0 0 0]
#  [0 0 1]
#  [1 1 1]]
# Note: Element-wise operations are fundamental in NumPy and are optimized for performance, allowing for efficient computations on large datasets.

# Practical example: Clipping values
clipped_data = np.clip(data, 30, 70)
print("Clipped data (values between 30 and 70):\n", clipped_data)
# Output:
# Clipped data (values between 30 and 70):
# [[30 30 30]
#  [40 50 60]
#  [70 70 70]]
# Note: Element-wise operations are fundamental in NumPy and are optimized for performance, allowing for efficient computations on large datasets.


# Matrix multiplications
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])
# Matrix multiplication using np.dot
C = np.dot(A, B)
print("Matrix multiplication using np.dot:\n", C)
# Output:
# [[ 58  64]
#  [139 154]]
# Matrix multiplication using @ operator
D = A @ B
print("Matrix multiplication using @ operator:\n", D)
# Output:
# [[ 58  64]
#  [139 154]]
# Element-wise multiplication (Hadamard product)
E = A * A
print("Element-wise multiplication (Hadamard product):\n", E)
# Output:
# [[ 1  4  9]
#  [16 25 36]]
# Note: Matrix multiplication is different from element-wise multiplication. Matrix multiplication follows the rules of linear algebra, while element-wise multiplication multiplies corresponding elements of the arrays.

# Transpose of a matrix
F = A.T
print("Transpose of matrix A:\n", F)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
# Note: Matrix multiplication is different from element-wise multiplication. Matrix multiplication follows the rules of linear algebra, while element-wise multiplication multiplies corresponding elements of the arrays.

# Inverse of a matrix
G = np.array([[1, 2],
              [3, 4]])
G_inv = np.linalg.inv(G)
print("Inverse of matrix G:\n", G_inv)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]
# Note: Matrix multiplication is different from element-wise multiplication. Matrix multiplication follows the rules of linear algebra, while element-wise multiplication multiplies corresponding elements of the arrays.

# Determinant of a matrix
det_G = np.linalg.det(G)
print("Determinant of matrix G:\n", det_G)
# Output:
# -2.0
# Note: Matrix multiplication is different from element-wise multiplication. Matrix multiplication follows the rules of linear algebra, while element-wise multiplication multiplies corresponding elements of the arrays.

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(G)
print("Eigenvalues of matrix G:\n", eigenvalues)
print("Eigenvectors of matrix G:\n", eigenvectors)
# Output:
# Eigenvalues of matrix G:
# [-0.37228132  5.37228132]
# Eigenvectors of matrix G:
# [[-0.82456484 -0.41597356]
#  [ 0.56576746 -0.90937671]]
# Note: Matrix multiplication is different from element-wise multiplication. Matrix multiplication follows the rules of linear algebra, while element-wise multiplication multiplies corresponding elements of the arrays.

# Singular Value Decomposition (SVD)
U, S, VT = np.linalg.svd(G)
print("U matrix from SVD of G:\n", U)
print("Singular values from SVD of G:\n", S)
print("VT matrix from SVD of G:\n", VT)
# Output:
# U matrix from SVD of G:
# [[-0.57604844 -0.81741556]
#  [-0.81741556  0.57604844]]
# Singular values from SVD of G:
# [5.4649857  0.36596619]
# VT matrix from SVD of G:
# [[-0.57604844 -0.81741556]
#  [ 0.81741556 -0.57604844]]
# Note: Matrix multiplication is different from element-wise multiplication. Matrix multiplication follows the rules of linear algebra, while element-wise multiplication multiplies corresponding elements of the arrays.


# Sorting and Searching
arr = np.array([3, 1, 4, 1, 5,
                9, 2, 6, 5, 3])
# Sorting the array
sorted_arr = np.sort(arr)
print("Sorted array:\n", sorted_arr)
# Output:
# Sorted array:
# [1 1 2 3 3 4 5 5 6 9]
# Searching for the index of a value
index_of_5 = np.where(arr == 5)[0]
print("Indices of value 5 in the array:\n", index_of_5)
# Output:
# Indices of value 5 in the array:
# [4 8]
# Finding the index to insert a value to keep the array sorted
index_to_insert_7 = np.searchsorted(sorted_arr, 7)
print("Index to insert value 7 to keep array sorted:\n", index_to_insert_7)
# Output:
# Index to insert value 7 to keep array sorted:
# 8

unique_elements = np.unique(arr)
print("Unique elements in the array:\n", unique_elements)
# Output:
# Unique elements in the array:
# [1 2 3 4 5 6 9]

arr2 = np.array([5, 6, 7, 8, 9])
intersection = np.intersect1d(arr, arr2)
print("Intersection of arr and arr2:\n", intersection)
# Output:
# Intersection of arr and arr2:
# [5 6 9]

original_array = np.array([[1, 2, 3, 4],
                            [5, 6, 7, 8]])
# Reshaping the array
reshaped_array = original_array.reshape(4, 2)
print("Reshaped array (4x2):\n", reshaped_array)
# Output:
# Reshaped array (4x2):
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# Resizing the array
resized_array = np.resize(original_array, (3, 4))
print("Resized array (3x4):\n", resized_array)
# Output:
# Resized array (3x4):
# [[1 2 3 4]
#  [5 6 7 8]
#  [1 2 3 4]]

# Flattening the array
flattened_array = original_array.flatten()
print("Flattened array:\n", flattened_array)
# Output:
# Flattened array:
# [1 2 3 4 5 6 7 8]

# Transposing the array
transposed_array = original_array.T
print("Transposed array:\n", transposed_array)
# Output:
# Transposed array:
# [[1 5]
#  [2 6]
#  [3 7]
#  [4 8]]

# Stacking arrays
array1 = np.array([[1, 2],
                    [3, 4]])
array2 = np.array([[5, 6],
                    [7, 8]])
stacked_array = np.vstack((array1, array2))
print("Vertically stacked array:\n", stacked_array)
# Output:
# Vertically stacked array:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

hstacked_array = np.hstack((array1, array2))
print("Horizontally stacked array:\n", hstacked_array)
# Output:
# Horizontally stacked array:
# [[1 2 5 6]
#  [3 4 7 8]]

# Splitting arrays
split_arrays = np.array_split(original_array, 2)
print("Split arrays:\n", split_arrays)
# Output:
# Split arrays:
# [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]