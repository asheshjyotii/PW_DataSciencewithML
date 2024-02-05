print("Right Half-Pyramid")
for i in range (0,6):
    for j in range(0,i):
        print("*",end=' ')
    print()

print("Left Half-Pyramid")
for i in range (1,5):
    for j in range(0,5-i):
        print(" ",end=' ')
    for k in range (1,i):
        print("*",end=' ')
    print()
