''' this is a string manipulation program that takes user input and counts the number of consonants in the string.   '''

s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Number of consonants:", count)