var1 = int(input("Enter a decimal number:"))
b = var1
binary = []
while(var1>0):
    binary.append(str(var1&1))
    var1 //=2
binary = ''.join(binary[::-1])
print(f"{b} -> {binary} ")