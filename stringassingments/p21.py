# Program 21: Find the length of a string without using len()

s = input("Enter a string: ")
count = 0

# Visit each character and increase the counter by one.
for ch in s:
    count += 1

print("Length:", count)
