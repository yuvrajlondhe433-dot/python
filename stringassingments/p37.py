# Program 37: Find the longest word in a sentence

s = input("Enter a sentence: ")
words = s.split()

# Check for an empty sentence before finding the longest word.
if words:
    longest = max(words, key=len)  # key=len compares words by their length.
    print("Longest word:", longest)
else:
    print("No words found")
