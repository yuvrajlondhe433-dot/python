# Program 16: Check whether a string contains only digits

s = input("Enter a string: ")

# isdigit() checks whether every character is a digit and the string is not empty.
if s.isdigit():
    print("String contains only digits")
else:
    print("String does not contain only digits")
