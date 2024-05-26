import pandas as pd

# Load the dataset, ensuring the header is included even when skipping the first 50 rows
data = pd.read_csv('People Data.csv', skiprows=range(1, 51))

# Only read the columns: 'Last Name', 'Gender', 'Email', 'Phone', and 'Salary'
data_filtered = data[['Last Name', 'Gender', 'Email', 'Phone', 'Salary']]

# Display the first 10 rows of the filtered dataset
print(data_filtered.head(10))

# Extract the 'Salary' column as a Series and display its last 5 values
salary_series = data_filtered['Salary']
print(salary_series.tail(5))


# Only read the columns: 'Last Name', 'Gender', 'Email', 'Phone', and 'Salary'
data_filtered = data[['Last Name', 'Gender', 'Email', 'Phone', 'Salary']]
print(data_filtered.head(10))

'''
Output:
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
$ python3 Q8.py
  Last Name  Gender  ...                   Phone  Salary
0    Zavala    Male  ...  001-859-448-9935x54536   80000
1     Carey  Female  ...    001-274-739-8470x814   70000
2     Hobbs  Female  ...        241.179.9509x498   60000
3    Reilly    Male  ...       207.797.8345x6177  100000
4    Conrad    Male  ...    001-599-042-7428x143   50000
5      Cole    Male  ...            663-280-5834   85000
6   Donovan    Male  ...                     NaN   65000
7    Little  Female  ...       125.219.3673x0076   60000
8    Dawson  Female  ...      650-748-3069x64529   60000
9      Page    Male  ...        849.500.6331x717   60000

[10 rows x 5 columns]
945     90000
946     50000
947     60000
948    100000
949     90000
Name: Salary, dtype: int64
  Last Name  Gender  ...                   Phone  Salary
0    Zavala    Male  ...  001-859-448-9935x54536   80000
1     Carey  Female  ...    001-274-739-8470x814   70000
2     Hobbs  Female  ...        241.179.9509x498   60000
3    Reilly    Male  ...       207.797.8345x6177  100000
4    Conrad    Male  ...    001-599-042-7428x143   50000
5      Cole    Male  ...            663-280-5834   85000
6   Donovan    Male  ...                     NaN   65000
7    Little  Female  ...       125.219.3673x0076   60000
8    Dawson  Female  ...      650-748-3069x64529   60000
9      Page    Male  ...        849.500.6331x717   60000

[10 rows x 5 columns]
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''