import numpy as np

# reshape
arr = np.array([1,2,3,4,5,6])
res = arr.reshape(2,3) # [[1 2 3] [4 5 6]]


# flatten as copy
arr2 = np.array([[1,2],[3,4]])
c_flat = arr2.flatten() # [1 2 3 4]

# ravel as view
arr3 = np.array([[1,2],[3,4]]) 
res = arr3.ravel(order='C') # order C means Row major and F means Column Major

# concatenate (join two or more arrays)
a = np.array([1,2,3])
b = np.array([4,5,6])
res = np.concatenate((a,b),axis=0) # [1 2 3 4 5 6]

# split(equal) or array_split(unequal)
ar = np.arange(10)
ar2 = np.arange(10)
a1,a2 = np.split(ar,2) # [0 1 2 3 4] [5 6 7 8 9]
b1 = np.array_split(ar2,3) # [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]

