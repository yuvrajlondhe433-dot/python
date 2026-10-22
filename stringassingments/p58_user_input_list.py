# 58. Take user input to create a list and display it
# Simulating user input for script demonstration:
user_input_str = "apple, banana, cherry, date" # e.g. input("Enter comma-separated items: ")
user_list = [item.strip() for item in user_input_str.split(",")]
print("User created list:", user_list)
