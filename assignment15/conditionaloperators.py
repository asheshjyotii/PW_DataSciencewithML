var1 = int (input("Enter the variable 1..\n"))
var2 = int (input("Enter the variable 2..\n"))
var3 = int (input("Enter the variable 3..\n"))
print("There are total of 3 conditional operators in python\n")

if(var1>var2 and var1>var3):
    print(f"The 'and' compares between two expressions if they both are correct if so it returns true...is {var1}>{var2} and {var1}>{var3} the answer is True\n")
else:
    print(f"The 'and' compares between two expressions if they both are correct if so it returns true...is {var1}>{var2} and {var1}>{var3} the answer is False\n")

if(var1>var2 or var1>var3):
    print(f"The 'or' compares between two expressions if any of them is correct it returns true...is {var1}>{var2} or {var1}>{var3} the answer is True\n")
else:
    print(f"The 'or' compares between two expressions if they both are correct if so it returns true...is {var1}>{var2} or {var1}>{var3} the answer is False\n")

if not (var1>var2):
    print(f"The 'not' checks if a single comparison is incorrect if yes it returns true... is {var1}>{var2} the answer is False")
else:
    print(
        f"The 'not' checks if a single comparison is incorrect if yes it returns true... is {var1}>{var2} the answer is True")