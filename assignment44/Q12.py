
import pandas as pd

# Load the dataset, ensuring the header is included even when skipping the first 50 rows
data = pd.read_csv('People Data.csv', skiprows=range(1, 51))
# a) Delete the 'Email', 'Phone', and 'Date of birth' columns from the dataset.
data = data.drop(columns=['Email', 'Phone', 'Date of birth'])

# b) Delete the rows containing any missing values.
data = data.dropna()

# c) Print the final output also
print(data)
'''
Output:
$ python3 Q12.py
     Index  ...  Salary
0       51  ...   80000
1       52  ...   70000
2       53  ...   60000
3       54  ...  100000
4       55  ...   50000
..     ...  ...     ...
945    996  ...   90000
946    997  ...   50000
947    998  ...   60000
948    999  ...  100000
949   1000  ...   90000

[950 rows x 7 columns]
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''
