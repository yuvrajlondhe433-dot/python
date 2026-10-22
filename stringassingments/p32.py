# Program 32: Check whether all cased characters are lowercase

s = input("Enter a string: ")

# islower() is True if the string has at least one cased character and all are lowercase.
if s.islower():
    print("String is lowercase")
else:
    print("String is not lowercase")
