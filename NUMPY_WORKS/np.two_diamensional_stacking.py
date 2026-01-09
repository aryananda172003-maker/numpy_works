import numpy as np
two_d_arr1=[
    [1,2],
    [3,4]
]
two_d_arr2=[
    [10,20],
    [30,40]

]
v_stack=np.vstack((two_d_arr1,two_d_arr2))
print(v_stack)#[[1 2]
                #[3 4]
                #[10 20]
                #[30 40]
h_stack=np.hstack((two_d_arr1,two_d_arr2))
print(h_stack)#[[1 2 10 20]
               # [3 4 30 40]