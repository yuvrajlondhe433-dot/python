# 80. Create a list and demonstrate all list methods
# Demonstrates: append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy

my_list = [10, 20, 30]
print("Initial list:", my_list)

# 1. append() - Adds element at end
my_list.append(40)
print("After append(40):", my_list)

# 2. extend() - Adds elements from iterable
my_list.extend([50, 60])
print("After extend([50, 60]):", my_list)

# 3. insert() - Inserts element at specific index
my_list.insert(1, 15)
print("After insert(1, 15):", my_list)

# 4. count() - Returns frequency of an element
my_list.append(20)
print("Count of 20:", my_list.count(20))

# 5. index() - Returns first index of element
print("Index of 30:", my_list.index(30))

# 6. remove() - Removes first occurrence of element
my_list.remove(20)
print("After remove(20):", my_list)

# 7. pop() - Removes and returns element at given index
popped = my_list.pop(2)
print(f"Popped element at index 2 ({popped}):", my_list)

# 8. reverse() - Reverses list in place
my_list.reverse()
print("After reverse():", my_list)

# 9. sort() - Sorts list in place
my_list.sort()
print("After sort():", my_list)

# 10. copy() - Returns a shallow copy
copied = my_list.copy()
print("Copied list:", copied)

# 11. clear() - Removes all elements
my_list.clear()
print("After clear():", my_list)
