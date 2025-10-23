import numpy as np

# Arithmetic Operations
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) # [5 7 9] np.add(a,b)
print(a-b) # [-3 -3 -3] np.subtract(a,b)
print(a*b) # [ 4 10 18] np.multiply(a,b)
print(a/b) # [0.25 0.4  0.5 ] np.divide(a,b)
print(a**2) # [1 4 9] np.power(a,2)
print(np.sum(a)) # 6
print(np.cumulative_sum(a)) # [1 3 6]
print(np.cumsum(a)) # [1 3 6]

# Trigonometric Function (Radian)
x = np.sin(90) # cos tan 
print(x) # 0.8939966636005579

# inverse
y = np.arcsin(1)
print(y) # 1.5707963267948966

# Degree to Radian
deg = np.array([0,90,180])
rad = np.deg2rad(deg) # rad2deg
print(rad) # [0. 1.57079633 3.14159265]

# Logarithmic
num = np.array([100,50,40])
print(np.log(num)) # [4.60517019 3.91202301 3.68887945]
print(np.log10(num)) # [2.  1.69897 1.60205999] 100/10 = 10 , 10/10 = 1 total 2
print(np.log2(num)) # [6.64385619 5.64385619 5.32192809]


# Comparison Operator (==,<,>,!=,<=,>=)
numbers = np.array([1,2,3,4,5,6])
print(numbers>3) # [False False False  True  True  True]
value = numbers > 2
print(numbers[value]) # [3 4 5 6]


# Boolean Condition
x = np.array([True,False,True])
print(np.all(x)) # False
print(np.any(x)) # True

# row / coumn wise, axis 0 = col, 1 = row
# np.all(numbers>3,axis = 0)


