# Create a list with 3 items
my_list = ["apple", "banana", "orange"]

# Add an item to the end of the list
my_list.append("grape")

# Remove the first item of the list
removed_item = my_list.pop(0)

# Determine if an item exists in the list
item_to_find = "banana"
if item_to_find in my_list:
    # If it does, display its index
    index = my_list.index(item_to_find)
    print(f"The index of '{item_to_find}' is: {index}")
else:
    # If it does not, give a user message
    print(f"'{item_to_find}' is not in the list.")

print("Updated list:", my_list)
