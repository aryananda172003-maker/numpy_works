"""
1 2 3
4 5 6
6 7 8
"""



import numpy as np
two_dimensional_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,8]


])
print(two_dimensional_array.ndim)
# size total number of elements
print(two_dimensional_array.size)
# shape will return number of rows and columns
print(two_dimensional_array.shape)