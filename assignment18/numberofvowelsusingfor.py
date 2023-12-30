str1 = input("Enter a string to find number of vowels:")
str1 = str1.lower()
# print(str1)
count = 0
for letter in range(len(str1)):
    vowel = ['a','e','i','o','u']
    for i in vowel:
        if (str1[letter] == i):
            count+=1

print(f"Therefore number of vowels are = {count}")