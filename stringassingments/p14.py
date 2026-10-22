# Program 14: Check whether a string is alphanumeric

s = input("Enter a string: ")

# isalnum() is True when all characters are letters or digits and the string is not empty.
if s.isalnum():
    print("String is alphanumeric")
else:
    print("String is not alphanumeric")
