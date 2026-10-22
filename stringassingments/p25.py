# Program 25: Extract only alphabets from a string

s = input("Enter a string: ")
result = ""

# Add letters to result and ignore digits, spaces, and punctuation.
for ch in s:
    if ch.isalpha():
        result += ch

print("Alphabets:", result)
