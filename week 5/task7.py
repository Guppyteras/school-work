# Ask the user for starting, ending, and increment numbers
starting_number = int(input("Enter the starting number: "))
ending_number = int(input("Enter the ending number: "))
increment_number = int(input("Enter the increment number: "))

# Output each number from 0 to starting number
print("Output each number from 0 to starting number:")
i = 0
while i <= starting_number:
    print(i, end=" ")
    i += 1
print()

# Output each number from 1 to starting number
print("Output each number from 1 to starting number:")
i = 1
while i <= starting_number:
    print(i, end=" ")
    i += 1
print()

# Output each number from starting number to ending number
print("Output each number from starting number to ending number:")
i = starting_number
while i <= ending_number:
    print(i, end=" ")
    i += 1
print()

# Output each number from starting number to ending number increasing by increment number
print(f"Output each number from {starting_number} to {ending_number} increasing by {increment_number}:")
i = starting_number
while i <= ending_number:
    print(i, end=" ")
    i += increment_number
print()
