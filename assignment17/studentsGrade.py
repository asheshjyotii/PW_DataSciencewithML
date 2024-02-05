var1 = float(input("Enter your obtained marks:"))

if ( var1 > 100.00 or var1 < 0.00  ):
    print("Invalid marks.")
elif ( var1 >= 90.00 ):
    print("Congratulations! You have obtained grade 'A'.")
elif ( var1 >= 80.00 ):
    print("Congratulations! You have obtained grade 'B'.")
elif ( var1 >= 70.00 ):
    print("Work Hard! You have obtained grade 'C'.")
elif ( var1 >= 60.00 ):
    print("Work Hard! You have obtained grade 'D'.")
elif ( var1 >= 50.00 ):
    print("Work Hard! You have obtained grade 'E'.")
elif ( var1 >= 40.00 ):
    print("Work Hard! You have obtained grade 'E-'.")
else:
    print("Sorry....You have failed, Try harder this time!")