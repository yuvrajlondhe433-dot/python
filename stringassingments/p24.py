# Program 24: Extract only digits from a string

s = input("Enter a string: ")
result = ""

# Add each digit to result and skip all non-digit characters.
for ch in s:
    if ch.isdigit():
        result += ch

print("Digits:", result)
