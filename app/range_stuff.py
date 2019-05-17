my_range = range(3)

# Basic for-loop
for i in my_range:
    print(i)

# Slicing stuff
my_list = [1, 2, 3, 4]

# Between item 1-> 3 counting from 0
print(my_list[1:4])

# Jump two between starting on second value
print(my_list[1:4:2])

# Remove the last value
print(my_list[:-1])

# Get the last value
print(my_list[-1])

# Revert
print(my_list[::-1])

# Count how many times a value exists in a list
print(my_list.count(2))
