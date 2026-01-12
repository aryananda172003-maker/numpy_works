import numpy as np
arr1=np.array([
    [1,2],
    [3,4]
])
arr2=np.array([
    [5,6],
    [7,7]


])
#(1*5+2*7) (1*6+2*7)=19 20
#(3*5+4*7) (3*6+4*7)=
matrix_mul=np.dot(arr1,arr2)
print(matrix_mul)