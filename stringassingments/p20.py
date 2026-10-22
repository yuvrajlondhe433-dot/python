# Program 20: Remove all occurrences of a given character from a string

s = input("Enter a string: ")
ch = input("Enter character to remove: ")

# replace() replaces every occurrence of the chosen character with an empty string.
print("Result:", s.replace(ch, ""))
