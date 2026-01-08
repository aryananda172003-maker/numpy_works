import numpy as np

leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])
# total leads gennerated each day

print(np.sum(leads,axis=0))

# total leads from each source
print(np.sum(leads,axis=1))

# highest lead day
day_wise_total=np.sum(leads,axis=0)
print(day_wise_total)# 180 231 195 198 95
max_total=np.max(day_wise_total)
print(max_total)#231
print(np.argmax(day_wise_total))# 1
#avg leads per source
print(np.average(leads,axis=1))
# avg leads per day
print(np.average(leads,axis=0))
#highest lead source
source_wise_total=np.sum(leads,axis=1)
print(source_wise_total)
print(np.argmax(source_wise_total))