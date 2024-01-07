# Took 30 min to complete this ...learned to iterate
# over dictionary you have you dictonary_name.items() and iterating over
# list you have to use enumerate for getting index also.

var1 =[]
rslt = {}

print("Enter 5 digits to found out the count of each digit")
for i in range(5):
    usr = int(input("Enter the digit {} :".format(i+1)))
    var1.append(usr)
length = len(var1)
for i,element in enumerate(var1):
    count =1
    if element not in rslt.keys():
        for j in range(i+1,length):
            if var1[j] == var1[i]:
                count+=1
        rslt[var1[i]] = count
print("{a:>7}{b:>6}".format(a='Digit',b='Count'))
for a,b in rslt.items():
    print("{a:>5}{b:>5}".format(a=a,b=b))