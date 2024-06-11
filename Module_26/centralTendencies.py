'''
In this the main focus is on using various libraries to get a jist of how they help in statistical operations.
The following librarys are tried:
1. numpy
2. statistics
3. scipy ->stats

'''

import numpy as np
age = [12,33,44,52,61,23,52]
print(np.mean(age))#-> 39.57142857142857
print(np.median(age))#->44.0
#print(np.mode(age)) -> mode is not present in numpy 
'''
so we now import and use scipy->stats library 
'''
from scipy import stats
print(stats.mode(age))#->ModeResult(mode=52, count=2)
#We can also use a library called statistics
import statistics
print(statistics.mean(age),statistics.median(age),statistics.mode(age))#->39.57142857142857 44 52