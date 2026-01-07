import numpy as np
array=np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]

])
print(array.ndim)
print(array.size)
print(array.shape)
# fetch 0th row
print(array[0])
# fetch 2 nd row
print(array[2])
# syntax arr[row,col]
#row slicing
#fetcing rows from 0 to 1
print(array[0:2])#[33 31 27]
                #[31 30 29]
print(array[:,0:2])
print(array[:,1:3])
print(array[:,1])
print(array[::2])
print(array[2,1])#32

print(array[1:3,1:3])
#skipp 2nd col print 0th 1th col
print(array[:,::2])