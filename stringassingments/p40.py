# Program 40: Count uppercase and lowercase letters separately

s = input("Enter a string: ")
upper = 0
lower = 0

# Count uppercase and lowercase letters separately; ignore digits and symbols.
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
