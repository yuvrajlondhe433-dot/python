# 75. Create a list and remove all even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_only = [num for num in numbers if num % 2 != 0]
print("List after removing even numbers:", odd_only)
