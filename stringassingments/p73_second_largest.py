# 73. Create a list and find the second largest number
numbers = [20, 67, 3, 99, 45, 99, 81]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]
print("Second largest number:", second_largest)
