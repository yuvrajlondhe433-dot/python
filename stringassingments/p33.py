# Program 33: Check whether all cased characters are uppercase

s = input("Enter a string: ")

# isupper() is True if the string has at least one cased character and all are uppercase.
if s.isupper():
    print("String is uppercase")
else:
    print("String is not uppercase")
