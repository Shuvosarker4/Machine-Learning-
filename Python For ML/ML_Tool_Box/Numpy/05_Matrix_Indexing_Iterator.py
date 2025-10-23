import numpy as np

# Diagonal Matrix
dm = np.diag([1,2,3,4]) # [[1 0 0 0][0 2 0 0][0 0 3 0][0 0 0 4]]

# Identity Matrix
im = np.eye(2) # [[1. 0.] [0. 1.]]

# Transpose Matrix
tp = np.array([[10,20],[40,50]]) # [[10 40] [20 50]]
res = tp.T

# Advance Indexing
lst = np.array([10,20,30,40])
values = lst[[0,3,1]] #[10 30 20]

# iterator
arr = np.array([[10,20],[40,50]])
for i in np.nditer(arr):
    print(i) # get all values without use nested loop




