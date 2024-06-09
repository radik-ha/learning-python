vows = "aeiou"

c = input("Enter A Character: ")

if c.isdigit():
    print("Please... Enter A Alphabet! Not A Number!")
elif c.lower() in vows:
    print(c,"is a Vowel")
else:
    print(c,"is a Consonant")
