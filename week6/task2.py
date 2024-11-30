# Create one list with 3 unique string values
list_one = ['apple', 'banana', 'cherry']

# Create another list with 3 unique integer values
list_two = [10, 20, 30]

# Create a set that contains the 6 values of the lists create above
set_one = set(list_one + list_two)

# Add any value to the SET created
set_one.add('orange')

# Remove any string value of the set created
set_one.discard('apple')

# Create a new set that takes any 3 values of the first set
set_two = set(list_one[1:] + list_two[1:])

# Output the values that are not in both sets
print("Values that are not in both sets:")
print(set_one.symmetric_difference(set_two))

# Using 1 for loop, output all the values of both sets
print("Values of both sets:")
for value in set_one:
    print(value)