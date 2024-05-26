import pandas as pd

# Load dataset
data = pd.read_csv('People Data.csv')

# Clean and transform the 'Phone' column
data['Phone'] = data['Phone'].str.replace(r'\D', '', regex=True).astype(float)

# Display table attributes and data types
print(data.dtypes)
'''
Output:
$ python3 Q7.py
Index              int64
User Id           object
First Name        object
Last Name         object
Gender            object
Email             object
Phone            float64
Date of birth     object
Job Title         object
Salary             int64
dtype: object
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''