''' this is a string manipulation program that takes user input and counts the number of vowels in the string.   '''

s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)