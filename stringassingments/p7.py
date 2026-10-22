# Program 7: Check whether a string ends with a given substring

s = input("Enter a string: ")
sub = input("Enter substring: ")

# endswith() checks whether the string ends with the given substring.
if s.endswith(sub):
    print("String ends with the given substring")
else:
    print("String does not end with the given substring")
