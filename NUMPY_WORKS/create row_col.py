"""
4 4 4 4 4
4 1 1  1 4
4 1 


"""
  
  







import numpy as np
fours_array=np.full((5,5),4)
print(fours_array)
ones_array=np.ones((3,3),dtype="int16")
print(ones_array)
ones_array[1,1]=100
print(ones_array)
fours_array[1:4,1:4]=ones_array
print(fours_array)

# np.random
rand_array=np.random.rand(2,3)
print(rand_array)
rand_int_array=np.random.randint(10,15 ,(2,3))
print(rand_int_array)