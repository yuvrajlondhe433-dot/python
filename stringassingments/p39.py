# Program 39: Check whether a string is a valid Python identifier

import keyword  # Used to check Python reserved keywords.

s = input("Enter an identifier: ")

# isidentifier() checks identifier syntax; keyword.iskeyword() rejects reserved words.
if s.isidentifier() and not keyword.iskeyword(s):
    print("Valid identifier")
else:
    print("Invalid identifier")
