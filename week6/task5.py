# Create a dictionary of your inventory
inventory = {
    'fruits': {'apple': 5, 'banana': 10},
    'vegetables': {'carrot': 20, 'spinach': 30},
    'dairy': {'milk': 100, 'cheese': 50}
}

# Create a dictionary of the vendor's inventory
vendor_inventory = {
    'fruits': {'banana': 15, 'orange': 20},
    'vegetables': {'carrot': 25, 'broccoli': 35},
    'dairy': {'milk': 100, 'yogurt': 50}
}

# Output the items that YOU have but the VENDOR does not have
difference = inventory.difference(vendor_inventory)
print("Items that I have but the vendor does not have:")
for category, items in difference.items():
    for item, quantity in items.items():
        print(f"{category.capitalize()}: {item.capitalize()}, quantity: {quantity}")

# Output the items that BOTH YOU and the VENDOR have
intersection = inventory.intersection(vendor_inventory)
print("\nItems that I have and the vendor also has:")
for category, items in intersection.items():
    for item, quantity in items.items():
        print(f"{category.capitalize()}: {item.capitalize()}, quantity (me): {quantity}, quantity (vendor): {vendor_inventory[category][item]}")

# Ask the user for an item
item = input("\nEnter an item: ").lower()

# Determine if the item is in STOCK (you have it)
if item in inventory:
    print(f"You have {item} in stock.")
else:
    print(f"You do not have {item} in stock.")

# Determine if vendor carries the item (vendor has it)
if item in vendor_inventory:
    print(f"The vendor carries {item}.")
else:
    print(f"The vendor does not carry {item}.")