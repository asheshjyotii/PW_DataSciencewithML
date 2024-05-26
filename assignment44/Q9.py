
import pandas as pd

# Load the dataset, ensuring the header is included even when skipping the first 50 rows
data = pd.read_csv('People Data.csv', skiprows=range(1, 51))
filtered_data = data[(data['Last Name'].str.contains('Duke')) & (data['Gender'] == 'Female') & (data['Salary'] < 85000)]
print(filtered_data)
'''
Output:
$ python3 Q9.py
     Index          User Id  ...        Job Title Salary
160    211  DF17975CC0a0373  ...  Producer, radio  50000
407    458  dcE1B7DE83c1076  ...        Herbalist  50000
679    730  c9b482D7aa3e682  ...     Nurse, adult  70000

[3 rows x 10 columns]
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''