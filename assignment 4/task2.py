import os
import sys

# Step 1: Ask the user for a path value
path = input("Enter a path: ")

# Step 1a: Determine if the path exists in the current filesystem
# i) If not, raise an exception
if not os.path.exists(path):
    raise FileNotFoundError(f"The path '{path}' does not exist in the current filesystem.")

# ii) If so, proceed to Step 2
# Step 2: Calculate and output the total number of
# i) All files and folders
all_files_and_folders = sum(os.path.isfile(f) or os.path.isdir(f) for f in os.listdir(path))
print(f"Total number of files and folders: {all_files_and_folders}")

# ii) Just the number of files
files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print(f"Total number of files: {files}")

# iii) Just the number of directories
directories = len([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print(f"Total number of directories: {directories}")