var1 = int(input("Enter variable 1\n"))
var2 = int(input("Enter variable 2\n"))
var3 = int(input("Enter variable 3\n"))
var1 = var2
if var1 is var2:
    print(f"linking first and second input var1 = var2 therefore variable 1={var1} and variable 2= {var2} shares object")
if var1 is not var3:
    print(f"{var1} and {var3} doesnot share object")
