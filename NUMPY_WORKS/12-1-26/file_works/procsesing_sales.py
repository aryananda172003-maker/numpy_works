import numpy as np
data=np.loadtxt("NUMPY_WORKS\\12-1-26\\file_works\\sales.csv",delimiter=",",skiprows=1,dtype="str")
print(data)
total=np.sum(data[:,3].astype("int"))
print(total)
min_unit_sold=np.min(data[:,3].astype("int"))
print(min_unit_sold)
max_unit_sold=np.max(data[:,3].astype("int"))
print(max_unit_sold)
avg_unit_sold=np.average(data[:,3].astype("int"))
print(avg_unit_sold,("average"))
#revenue
revenue=data[:,3].astype("int")*data[:,4].astype("float")
print(revenue)
# total revenue
print(np.sum(revenue))
# unit sold >8
print(data[data[:,3].astype("int")>8])

# category==electronics
print("electronics",data[data[:,2]=="Electronics"])
print("============")
#discount own
print(data[:,1], data[:,4].astype("int")-100)
#update discount 100 sir
data[:,4]=data[:,4].astype("int")-100
print("discount",data)
# total revenue of north region
north=data[data[:,-1]=="North"]
print(north)
revenue=north[:,3].astype("int")*north[:,4].astype("int")
print(np.sum(revenue))

