# Program 30: Check whether a string is in title case

s = input("Enter a string: ")

# istitle() checks whether each word follows Python's title-case rules.
if s.istitle():
    print("String is in title case")
else:
    print("String is not in title case")
