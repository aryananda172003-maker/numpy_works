
import numpy as np
sales_report=np.array([
    [
        [10,11],
        [12,13]
    ],
    [
        [100,110],
        [120,130]
    ],

])
print(sales_report.ndim)
print(sales_report.shape)
print(sales_report[1,0,1])#110 level=1 row=0 col=1
print(sales_report[0,1,1])#13
#update13=14 level=0 r=1 col=1
sales_report[0,1,1]=14
print(sales_report)
# update 10=15
sales_report[0,0,0]=15
print(sales_report)

#  2 type stacking horizotal and vertical
arr1=np.array([1,2,3,4])
arr2=np.array([10,20,30,40])
# vertical stacking
v_stack=np.vstack((arr1,arr2))
print(v_stack)
# horizontal stacking
h_stack=np.hstack((arr1,arr2))
print(h_stack)
# reshaping 
arr=np.array([1,3,5,6,7,8])
new_array=np.reshape(arr,shape=(3,2))
print(new_array)
new_array=np.reshape(arr,shape=(2,3))
print(new_array)


# filtering

productivity = np.array([
    #d
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])
# print working hrs of frst employee
print(productivity[0,:])
# print working hrs of 3rd employee
print(productivity[2,:])
# print frst two employees wotging hr <7
last_two_employees_w_hrs=productivity[0:2,:]
print(last_two_employees_w_hrs)
print(last_two_employees_w_hrs[last_two_employees_w_hrs<7])
last_two_employees_w_hrs[last_two_employees_w_hrs<7]=0
print(last_two_employees_w_hrs)
productivity[productivity>8]=10
print(productivity)
#broadcasting
new=productivity[0,:]+10
print(new)#[18 17 18 10 17 18 20 18 17 18]
# create row,col
array=np.full((5,3),15)
print(array)
array=np.ones((3,2),dtype="int16")
print(array)
