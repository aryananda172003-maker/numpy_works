import numpy as np
# task2 [-ve,+ve]
array=np.array([-1,2,3,-1,5,-6])
print(np.where(array>0,"+ve","-ve"))