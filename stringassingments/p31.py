# Program 31: Remove punctuation marks from a string

import string  # Provides the punctuation characters used in the standard ASCII set.

s = input("Enter a string: ")
result = ""

# Keep characters that are not listed in string.punctuation.
for ch in s:
    if ch not in string.punctuation:
        result += ch

print("Without punctuation:", result)
