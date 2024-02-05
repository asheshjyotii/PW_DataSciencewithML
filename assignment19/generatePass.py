import string,random
special = "!@#$%^&*()_-+=[]{}|;:'\",.<>/?`~"
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digit = string.digits
a=""

passwrd = (random.choices(lowercase,k=3)+random.choices(uppercase,k=3)+random.choices(digit,k=3)+random.choices(special,k=3))

print("Your pass words is:")
# passwrd = random.choices(passwrd,k=12)
# print(len(passwrd))
for i in passwrd:
    a = a+i
print(a)