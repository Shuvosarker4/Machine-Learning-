import numpy as np

all_zero = np.zeros((2,3))      # [[0. 0. 0.] [0. 0. 0.]]
all_one = np.ones((2,3))        # [[1. 1. 1.] [1. 1. 1.]]
all_empty = np.empty((2,3))     # [[0. 0. 0.] [0. 0. 0.]]
all_full = np.full((2,3),fill_value=np.inf) # [[inf inf inf] [inf inf inf]]

exist_shape = np.array([[10,20],[30,40]]) # existing shape (2,2)

new_shape = np.ones_like(exist_shape)
print(new_shape) # [[1 1] [1 1]]