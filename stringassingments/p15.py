# Program 15: Check whether a string contains only alphabets

s = input("Enter a string: ")

# isalpha() is True when every character is a letter and the string is not empty.
if s.isalpha():
    print("String contains only alphabets")
else:
    print("String does not contain only alphabets")
