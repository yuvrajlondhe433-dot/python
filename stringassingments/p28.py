# Program 28: Count the number of words in a sentence

s = input("Enter a sentence: ")

# split() returns a list of words; len() counts the list items.
words = s.split()
print("Number of words:", len(words))
