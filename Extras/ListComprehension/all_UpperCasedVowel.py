string1 = 'Hello World'

vowels = [x.upper() for x in string1 if x.lower() in 'aeiou' ]
print(vowels)