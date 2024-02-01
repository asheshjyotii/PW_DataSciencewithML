def my_generator():
    a = 1
    while True:
        yield a
        a=a+1

for i in range(11):
    print(next(my_generator()))