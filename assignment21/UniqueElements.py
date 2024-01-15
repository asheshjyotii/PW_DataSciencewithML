list1 = [1,2,1,3,3,4,4,4]
unique =[]
for i in list1:
    if i not in unique:
        unique.append(i)
print(unique)