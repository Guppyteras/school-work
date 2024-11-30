# Create an empty list
user_inputs = []

# Ask the user for input 5 times
for _ in range(5):
    new_input = input("Enter any input: ")
    
    # Only add the input to the list if it does NOT already exist
    if new_input not in user_inputs:
        user_inputs.append(new_input)

print("Unique inputs:", user_inputs)
