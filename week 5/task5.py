# Initialize an empty list to store user inputs
user_inputs = []

# Ask the user for input 3 times
for _ in range(3):
    user_input = input("Enter any input: ")
    user_inputs.append(user_input)

# Convert the inputs into a tuple
input_tuple = tuple(user_inputs)

# Output the tuple
print("Tuple from user inputs:", input_tuple)
