# Program 36: Remove duplicate characters from a string

s = input("Enter a string: ")
result = ""

# Add a character only the first time it appears, preserving the original order.
for ch in s:
    if ch not in result:
        result += ch

print("Without duplicates:", result)
