# 76. Create a list and remove all odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_only = [num for num in numbers if num % 2 == 0]
print("List after removing odd numbers:", even_only)
