# My Name : George Hany

# How to create an empty and a full Numpy array ?

# First, to create an empty numpy array we use "numpy.empty()" function with a specified shape.
# An empty NumPy array is an array that is initialized with arbitrary values.

# Examples :

# 1)

import numpy as np
arr_1 = np.empty((3, 4))
print('Empty arr_1')
print()
print(arr_1)
print()

# 2)

arr_2 = np.empty((3, 4), dtype = int)
print('Empty arr_2')
print()
print(arr_2)
print()
print()

# --------------------------------------

# Second, to create a full NumPy array, we can use the "numpy.full()" function.
# A full NumPy array is an array where all the elements have the same predefined value.
# This is useful when you want to initialize an array with a specific value.

# Examples :

# 1)

import numpy as np
arr_1 = np.full((3, 4), 5)
print('Full arr_1')
print()
print(arr_1)
print()
print()

# 2)

arr_2 = np.full((6, 2), 7, dtype = int)
print('Full arr_2')
print()
print(arr_2)
