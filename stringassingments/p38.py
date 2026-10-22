# Program 38: Find the shortest word in a sentence

s = input("Enter a sentence: ")
words = s.split()

# Check for an empty sentence before finding the shortest word.
if words:
    shortest = min(words, key=len)  # key=len compares words by their length.
    print("Shortest word:", shortest)
else:
    print("No words found")
