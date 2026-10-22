# Program 26: Find the first and last occurrence of a character

s = input("Enter a string: ")
ch = input("Enter a character: ")

# find() returns the first index; rfind() returns the last index.
# Both return -1 if the character is not found.
print("First occurrence:", s.find(ch))
print("Last occurrence:", s.rfind(ch))
