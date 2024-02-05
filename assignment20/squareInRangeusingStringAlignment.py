var1 = int(input("Enter the number upto which squares to be printed:"))
print("{a:>7}{c:>10}".format(a='Digit', c='Squared'))
for i in range(1,var1+1):
    print("{a:>5}{c:>9}".format(a=i,c=i**2))