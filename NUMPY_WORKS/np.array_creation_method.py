# array creation method:
"""
np.array()
np.ones((r,c))
np.zeros((r,c))
np.full((r,c),value)
np.random.rand(r,c)
np.rand.randint(low,high),(r,c)
argmax:return index
axis=1[row]
axis=0[col]
np.sum
np.max
np.min
np.avg
"""






import numpy as np
zeros_array=np.zeros((2,3),dtype="int16")
print(zeros_array)
ones_array=np.ones((4,4),dtype="int16")
print(ones_array)
five_array=np.full((2,3),5)
print(five_array)
