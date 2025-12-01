# Broadcasting example in NumPy
import numpy as np
# Create a 2D array (matrix) of shape (3, 4)
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
# Create a 1D array (vector) of shape (4,)
b = np.array([10, 20, 30, 40])
# Add the 1D array to the 2D array using broadcasting
C = A + b
print("Result of broadcasting addition:\n", C)
# Output:
# Result of broadcasting addition:
# [[11 22 33 44]
#  [15 26 37 48]
#  [19 30 41 52]]

# Create another 1D array (vector) of shape (3,)
d = np.array([100, 200, 300])
# Add the 1D array to the 2D array using broadcasting
E = A + d[:, np.newaxis]  # Reshape d to (3, 1) for broadcasting
print("Result of broadcasting addition with reshaped vector:\n", E)
# Output:
# Result of broadcasting addition with reshaped vector:
# [[101 102 103 104]
#  [205 206 207 208]
#  [309 310 311 312]]

# Demonstrating broadcasting with different shapes
F = np.array([[1], [2], [3]])  # Shape (3, 1)
G = np.array([10, 20, 30, 40])  # Shape (4,)
H = F + G  # Broadcasting to shape (3, 4) 
print("Result of broadcasting with different shapes:\n", H)
# Output:
# [[11 21 31 41]
#  [12 22 32 42]
#  [13 23 33 43]]

# Note: Broadcasting allows NumPy to perform operations on arrays of different shapes in a way that makes sense mathematically, without the need for explicit replication of data.
