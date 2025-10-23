import numpy as np

# ndArray generate with random value
all_float = np.random.rand(2,3) # (2,3) shape value from 0.__ float
all_int = np.random.randint(1,10,(2,3)) # (2,3) shape value from 1 to 9 range
all_float_range = np.random.uniform(50,100,(3,3,4)) # 3D from 50.00 to 99.99 range

# ndArray generate with a given range value arange(start,end,step)
arr = np.arange(1,10,1) # generate number
arr1 = arr.reshape(3,3) # create matrix (3,3) shape

# pick 5 point from 0-10 range 
five_point = np.linspace(0,10,5) # end include [ 0. 2.5  5.  7.5  10. ]

# pick 5 point with log base 10^ 10^...
pick_five_log = np.logspace(0,4,5,base=10) # [1.e+00 1.e+01 1.e+02 1.e+03 1.e+04]

