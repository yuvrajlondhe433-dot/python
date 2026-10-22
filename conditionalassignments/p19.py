ch = input("Enter a character: ").lower()

if ch in 'aeiou' and len(ch) == 1:
    print("Vowel")
else:
    print("Consonant")
