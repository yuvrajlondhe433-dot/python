# Program 23: Check whether a string is a palindrome

s = input("Enter a string: ")
s = s.lower()  # Convert to lowercase so the check ignores letter case.

# A palindrome is the same when read forwards and backwards.
if s == s[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
