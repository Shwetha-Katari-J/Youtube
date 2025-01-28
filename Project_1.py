import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr_2d)

# Access elements
print("\nElement at (1, 2):", arr_2d[1, 2])  # Row 1, Column 2

# Reshape an array
reshaped = arr.reshape((5, 1))
print("\nReshaped Array:\n", reshaped)
