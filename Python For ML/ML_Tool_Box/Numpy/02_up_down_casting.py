import numpy as np

arr = np.array([10,20.50,30,40])

# bool --> int
# int --> float
# float --> complex

# example of int to float 
print(arr.dtype)

# change data type by using astype
print(arr.astype(np.int64)) # [10 20 30 40]

