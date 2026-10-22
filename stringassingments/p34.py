# Program 34: Find the ASCII value of each character in a string

s = input("Enter a string: ")

# ord() returns the Unicode code point; for ASCII characters, this is the ASCII value.
for ch in s:
    print(ch, "=", ord(ch))
