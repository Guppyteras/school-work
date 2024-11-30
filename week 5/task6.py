# Ask the user for starting, ending, and increment numbers
starting_number = int(input("Enter the starting number: "))
ending_number = int(input("Enter the ending number: "))
increment_number = int(input("Enter the increment number: "))

print("Output each number from 0 to starting number:")
for i in range(starting_number + 1):
    print(i, end=" ")
print()

print("Output each number from 1 to starting number:")
for i in range(1, starting_number + 1):
    print(i, end=" ")
print()

print("Output each number from starting number to ending number:")
for i in range(starting_number, ending_number + 1):
    print(i, end=" ")
print()

print(f"Output each number from {starting_number} to {ending_number} increasing by {increment_number}:")
for i in range(starting_number, ending_number + 1, increment_number):
    print(i, end=" ")
print()
