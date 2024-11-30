import os

# Step 1: Ask the user for a filename
filename = input("Enter a filename: ")

# Step 1a: Check to determine if filename has an extension
if "." not in filename:
    # i) If not, add a “.txt” extension
    filename += ".txt"

# Step 1b: Check to determine if the filename already exists
# i) If so, raise an exception
if os.path.exists(filename):
    raise FileExistsError(f"The file '{filename}' already exists in the current working directory.")

# Step 2: Create a file with the name the user inputted
with open(filename, 'a') as file:
    pass

# Step 3: Ask the user for content
content = input("Enter content (at least 10 characters): ")

# Step 3a: Ensure that the content is at least 10 characters
# i) If not, raise an exception
if len(content) < 10:
    raise ValueError("The content should be at least 10 characters long.")

# ii) If so, proceed to Step 4
# Step 4: Append the data entered in Step 3) to the file the user inputted in Step 1
with open(filename, 'a') as file:
    # Add a new line character at the end of the user input
    file.write(content + "\n")