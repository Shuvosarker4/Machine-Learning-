import numpy as np

number = np.array([5,1,4,2])
# Sort copy
copy_num = np.sort(number) # [1 2 4 5]
number.sort() # [1 2 4 5] original too
des = np.sort(number)[::-1] # [5 4 2 1]
# for 2D array use axis np.sort(arr,axis = 1)


# Searching
numbers = np.array([10,20,30,40,50])
res = np.where(numbers>25, "HIGH","LOW") # ['LOW' 'LOW' 'HIGH' 'HIGH' 'HIGH']
print(np.where(numbers>25)) # (array([2, 3, 4]),)

# max & min return index number
mx = np.argmax(numbers) # 4
mn = np.argmin(numbers) # 0

# count_nonzero return number, unique
num = np.arange(1,100)
even = np.count_nonzero(num%2 ==0) # 49 even

numm = np.array([0,1,1,2,2,3,4,5,5,3])
print(np.unique(numm)) # [0 1 2 3 4 5]
num,count = np.unique(numm,return_counts=True)
print(num,count) # num = [0 1 2 3 4 5] count = [1 2 2 2 1 2]

