import numpy as np

one = np.array([10,20,30]) # one dimensional array

two = np.array([[10,20,30],[40,50,60]]) # two dimension

three = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) # three dimension

# check dimension on the ndArray
print(one.ndim)
# check size of the ndArray / total elements
print(three.size)
# check the data type of ndArray
print(two.dtype)
# check the shape of the ndArray / row * col, return tuple (2,3)
print(two.shape)