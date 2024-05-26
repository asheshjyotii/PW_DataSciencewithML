
import pandas as pd
import numpy as np

# Load the dataset, ensuring the header is included even when skipping the first 50 rows
data = pd.read_csv('People Data.csv', skiprows=range(1, 51))
df = pd.DataFrame(np.random.randint(1, 7, size=(7, 5)))
print(df)
'''
Output:
$ python3 Q10.py                              
   0  1  2  3  4
0  5  6  4  3  3
1  4  4  6  6  5
2  3  1  3  6  5
3  1  1  5  2  5
4  1  3  2  4  6
5  5  5  3  1  5
6  6  2  1  4  1
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''