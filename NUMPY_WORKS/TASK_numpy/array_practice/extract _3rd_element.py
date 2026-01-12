
import numpy as np
#1D Array Practice

#1. Given arr = np.array([3, 6, 9, 12, 15, 18]), extract the 3rd element.
arr=np.array([3,6,9,12,15,18])
print(arr[2])#9

#2. From arr = np.array([5, 10, 15, 20, 25, 30]), extract elements from index 2 to 4.
arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[2:5])#[15 20 25]



#3. Given arr = np.array([2, 4, 6, 8, 10, 12]), extract all even-indexed elements.

arr = np.array([2, 4, 6, 8, 10, 12])
print(arr[::2])#[2 6 10]

#4. From arr = np.array([11, 22, 33, 44, 55]), select elements greater than 30.
arr = np.array([11, 22, 33, 44, 55])
print(arr[arr>30])#[33 44 55]

#5. Given arr = np.array([7, 14, 21, 28, 35]), replace all numbers greater than 20 with -1.
arr = np.array([7, 14, 21, 28, 35])
greater=arr[arr>20]
print(greater)
arr[2:5]=-1
print(arr)#[7 14 -1 -1 -1]

#6. From arr = np.array([1, 2, 3, 4, 5]), pick elements at positions [0, 2, 4] using advanced indexing.
arr = np.array([1, 2, 3, 4, 5])
print(arr[::2])#[1 3 5]

#7. Let arr = np.array([10, 20, 30, 40]). Multiply every element by 2 using broadcasting.

arr = np.array([10, 20, 30, 40])
new_arr=arr*2
print(new_arr)#[20 40 60 80]
#8. Given arr = np.array([100, 200, 300, 400, 500]), reverse the array using advanced indexing.

arr = np.array([100, 200, 300, 400, 500])
print(arr[::-1])




#✅ 2D Array Practice

#9. Let arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). Extract the first row.

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr[0])#[1 2 3]
#10. From the same array, extract the last column.
print(arr[:,2])


#11. From arr = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), select elements greater than 10.

arr = np.array([[2, 4, 6],
                [8, 10, 12],
                [14, 16, 18]])
print(arr[arr>10])#[12 14 16 18]

#12. Use advanced indexing to select elements at positions (0,0), (1,1), and (2,2) from the above array.

print(arr[:,0])#[2 8 14]
#13. Given arr = np.array([[1, 2], [3, 4], [5, 6]]), multiply every element by 5 using broadcasting.
arr = np.array([[1, 2], [3, 4], [5, 6]])
new_arr=arr*5
print(new_arr)#[5 10]
                #[25 30]]

#14. From arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), extract the subarray [[3,4],[7,8]].
arr = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print(arr[0:2,2:4])#[3 4]
                    #[7 8]]



#15. Given arr = np.array([[2, 4], [6, 8], [10, 12]]), multiply only the first column by 10 using broadcasting.

arr = np.array([[2, 4],
                [6, 8],
                [10, 12]])
new_arr=arr[:,0]*10
print(new_arr)#[20 60 100]



