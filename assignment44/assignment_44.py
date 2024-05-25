import numpy as np

# Method 1: Using np.array
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print("Method 1:", array1)
'''
Output 1:
Method 1: [[1 2 3]
 [4 5 6]]
'''

# Method 2: Using np.ones and scalar multiplication
array2 = np.ones((2, 3)) * np.array([1, 2, 3])
print("Method 2:", array2)
'''
Output 2:
Method 2: [[1. 2. 3.]
 [1. 2. 3.]]
'''

# Method 3: Using np.full
array3 = np.full((2, 3), [1, 2, 3])
print("Method 3:", array3)
'''
Output 3:
Method 3: [[1 2 3]
 [1 2 3]]
'''
