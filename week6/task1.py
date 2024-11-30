# Create a set of numbers between 10 and 20
set_one = {x for x in range(10, 21)}

# Create another set of numbers between 5 and 15
set_two = {x for x in range(5, 16)}

# Output the difference of the two sets
print("Difference of the two sets:")
print(set_one.difference(set_two))
print(set_two.difference(set_one))

# Output the common numbers of the two sets
print("Common numbers of the two sets:")
print(set_one.intersection(set_two))

# Iterate through each value of sets one and two
print("Iterate through each value of sets one and two:")
for num in set_one.union(set_two):
    print(num)