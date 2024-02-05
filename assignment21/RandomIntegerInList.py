import random

my_list = []


for _ in range(5):
    random_number = random.randint(1, 10)
    my_list.append(random_number)

print(my_list)
