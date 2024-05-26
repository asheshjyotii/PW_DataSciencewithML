import numpy as np
array = np.random.randint(1, 11, (3, 3, 3))
print("3D Array:", array)

# a) Find the indices of the maximum values along each depth level (third axis).
max_indices = np.argmax(array, axis=2)
print("Indices of Maximum Values:", max_indices)

# b) Element-wise multiplication between two arrays
array2 = np.random.randint(1, 11, (3, 3, 3))
elementwise_multiplication = array * array2
print("Element-wise Multiplication:", elementwise_multiplication)
'''
Output:
$ python3 Q6.py 
3D Array: [[[ 5  5  9]
  [ 9  7  1]
  [ 8  6  4]]

 [[10  9  5]
  [ 2  8  3]
  [ 8  4  6]]

 [[ 4  4  5]
  [10  7  9]
  [ 4  2  2]]]
Indices of Maximum Values: [[2 0 0]
 [0 1 0]
 [2 0 0]]
Element-wise Multiplication: [[[ 50  45  18]
  [ 18  70   3]
  [ 16  54  36]]

 [[ 40  72  35]
  [ 18   8   6]
  [ 24  20  18]]

 [[ 20  40  20]
  [100  14  27]
  [ 12  16   6]]]
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''