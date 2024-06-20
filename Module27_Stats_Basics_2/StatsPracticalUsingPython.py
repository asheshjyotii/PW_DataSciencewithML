#%%

data = [1,2,5,12,77,44,3]
print(max(data)-min(data))

# %%
import numpy as np
data = [1,2,5,12,77,44,3]
#here np.percentile accepts some patameters among which a is for array of number & q is for a list of quartiles to output the value
print(np.percentile(a=data,q=[0,25,50,75,100])) #[ 1.   2.5  5.  28.  77. ]
# %%
import seaborn as sea
data = [1,2,5,12,77,44,3]
sea.boxplot(data)
# %%
#Standard Deviation
import numpy as np
data = [1,2,5,12,77,44,3]
np.std(data) #26.954231805876013
# %%
#Variance
import numpy as np
data = [1,2,5,12,77,44,3]
np.var(data) #726.5306122448981
# %%
#Sets
s = {1,1,2,2,2,4,3,5}
print(s) #{1, 2, 3, 4, 5}
print(s[0]) #TypeError: 'set' object is not subscriptable
# %%
#Set intersection
set1 = {34,67,78,100}
set2 = {67,68,34}
# there are two ways of getting intersection
print(set1 & set2) #{34, 67}

# or

print(set1.intersection(set2)) #{34, 67}
# %%
#Set Union
set1 = {34,67,78,100}
set2 = {67,68,34}
# there are two ways of getting union
print(set1 | set2) #{34, 67, 100, 68, 78}

# or

print(set1.union(set2)) #{34, 67, 100, 68, 78}
# %%
#Set difference
set1 = {34,67,78,100}
set2 = {67,68,34}
# there are two ways of getting difference
print(set1 - set2) #{100, 78}

# or

print(set1.difference(set2)) #{100, 78}
# %%
#subset & superset
set1 = {34,67,78,100}
set2 = {67,78,34}

print(set1.issubset (set2)) #False

#&

print(set1.issuperset(set2)) #True
# %%
#Set symmetric difference
set1 = {34,67,78,100}
set2 = {67,68,34,112}
# there are two ways of getting symmeric difference
print(set1 ^ set2) #{112, 100, 68, 78}

# or

print(set1.symmetric_difference(set2)) #{112, 100, 68, 78}
# %%
