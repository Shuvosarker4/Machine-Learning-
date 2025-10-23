import numpy as np

# Linear Algebra
a = np.array([1,2,3])
b = np.array([4,5,6])

# dot multiplication
print(np.dot(a,b)) # 32

arr = np.array([[10,20],[40,50]])
# trace
print(np.trace(arr)) # 60
# matrix rank
print(np.linalg.matrix_rank(a)) # 1
# determinant != 0
print(np.linalg.det(arr)) # -299.99999999999994
# np.linalg.inv() for inverse
# np.linalg.solve() for solve
# num.T for Transpose
# np.diag([1,2,3,4]) for diagonal
# np.eye(2) for Identity Matrix

# statistical math ---
# np.mean() for Average
# np.median for Middle value
# np.std() for Standar Deviation
# np.corrcoef() for correlation coefficient
 
