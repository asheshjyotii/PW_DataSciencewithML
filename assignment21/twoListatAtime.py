# Iterate of 2 or more list at a time and print the values
name = ['ashesh', 'Anwesha', 'Sunita']
age = [20, 21, 18]
weight = ['68 kg', '38 kg', '43 kg']

print("|---------|-----|------|")
print("|   name  | age |weight|")
print("|---------|-----|------|")
# Use zip to iterate over the three lists simultaneously
for name, age, weight in zip(name, age, weight):
    print(f"|{name.center(9)}|{str(age).center(5)}|{str(weight).center(6)}|")

print("|---------|-----|------|")