# Program 29: Replace a word with another word in a sentence

s = input("Enter a sentence: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

# replace() substitutes every matching occurrence of old with new.
print("Result:", s.replace(old, new))
