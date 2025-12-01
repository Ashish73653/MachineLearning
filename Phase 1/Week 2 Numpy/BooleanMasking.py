import numpy as np
# Create a 1D NumPy array
array_1d = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print("Original 1D array:\n", array_1d)
# Boolean masking to filter elements greater than 25
bool_mask = array_1d > 25
print("Boolean mask (elements > 25):\n", bool_mask)
filtered_array = array_1d[bool_mask]
print("Filtered array (elements > 25):\n", filtered_array)

# Use and or not operations with boolean masks
mask_greater_20 = array_1d > 20
mask_less_40 = array_1d < 40
combined_mask = mask_greater_20 & mask_less_40
print("Combined mask (20 < elements < 40):\n", combined_mask)
filtered_combined = array_1d[combined_mask]
print("Filtered array (20 < elements < 40):\n", filtered_combined)
# Negating a boolean mask
negated_mask = ~ (array_1d > 30)
print("Negated mask (elements <= 30):\n", negated_mask)
filtered_negated = array_1d[negated_mask]
print("Filtered array (elements <= 30):\n", filtered_negated)