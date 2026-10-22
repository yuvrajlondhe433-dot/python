# 77. Create a list and check palindrome list
my_list = [1, 2, 3, 2, 1]
is_palindrome = my_list == my_list[::-1]
print(f"Is {my_list} a palindrome?", is_palindrome)
