import numpy as np
array = np.random.randint(1, 11, (5, 6))
print("Original Array:", array)

# a) Extract all even integers from array
even_integers = array[array % 2 == 0]
print("Even Integers:", even_integers)

# b) Extract all odd integers from array
odd_integers = array[array % 2 != 0]
print("Odd Integers:", odd_integers)
'''
Output:
$ python3 Q5_Random_integer.py                     
Original Array: [[ 5  5  8  5  2  6]
 [ 9  1  9  3  3  6]
 [ 8  3 10  3  2 10]
 [ 2  8  1  9 10  8]
 [ 9  7  3  8  6  1]]
Even Integers: [ 8  2  6  6  8 10  2 10  2  8 10  8  8  6]
Odd Integers: [5 5 5 9 1 9 3 3 3 3 1 9 9 7 3 1]
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''
