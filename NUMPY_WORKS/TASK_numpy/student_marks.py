import numpy as np
array=np.array([
    [43,42,45,34,23],#vipin
    [23,45,45,34,37],#hari
    [37,38,39,40,45]#cibin
 #math#eng#mal#cs#so

])
print(array.ndim)
print(array.size)
print(array.shape)

#display marks of hari
print(array[1]) #[23 45 45 34 37]

#display maths marks of hari
print(array[1,0])#23

# display malayalam marks of all student
print(array[:,2])#[45 45 39]

# display malayalam and cs marks of all student
print(array[:,2:4])#[45 34]
                    #[45 34]
                    #[39 40]

#display heng and malayalam marks of hari and cibin
print(array[1:3,1:3])#[45 45]
                    #[38 39]


#own question
#display all students eng marks
print(array[:,1])#[42 45 38]

# display vipin and cibin all marks
print(array[:,0::4])#[43 23]
                    #[23 37]
                    #[37 45]