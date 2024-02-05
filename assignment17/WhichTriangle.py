print("Enter the sides of a triangle to know its type.\n")
var1 = float(input("Enter one side of the triangle:"))
var2 = float(input("Enter another side of the triangle:"))
var3 = float(input("Enter another side of the triangle:"))

if (var1 == var2 and var1 == var3):
    print("Equilateral Trinagle.")
elif (var1 == var2 or var1 == var3 or var2 == var3):
    print("Isoceles Trinagle.")
else:
    print("Its a Scalene Triangle with no equal sides.")