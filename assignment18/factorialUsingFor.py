var1 = int(input("Enter a number:"))
fact = 1
for i in range(var1,0,-1):
    fact *= i
    # i -= 1
print(f"The factorial of {var1} = {fact}")
