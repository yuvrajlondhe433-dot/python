# Program 27: Check whether a word exists in a sentence

s = input("Enter a sentence: ")
word = input("Enter a word: ")

# split() creates words, so this checks for a whole-word match.
if word in s.split():
    print("Word exists in the sentence")
else:
    print("Word does not exist in the sentence")
