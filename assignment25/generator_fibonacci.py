def my_generator():
    a,b = 0,1
    while True:
        nexterm = a + b
        yield nexterm

        a=b
        b = nexterm


fib = my_generator()
for i in range(11):

    print(next(fib))
