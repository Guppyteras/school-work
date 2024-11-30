import os

# Create sub-directories
d1_path = 'd1'
d2_path = 'd1/d2'
d3_path = 'd1/d2/d3'

if not os.path.exists(d1_path):
    os.makedirs(d1_path)
if not os.path.exists(d2_path):
    os.makedirs(d2_path)
if not os.path.exists(d3_path):
    os.makedirs(d3_path)

# Add empty text files
file_names = ['file1.txt', 'file2.txt']

for file_name in file_names:
    with open(os.path.join(d1_path, file_name), 'w') as f:
        pass

    with open(os.path.join(d2_path, file_name), 'w') as f:
        pass

    with open(os.path.join(d3_path, file_name), 'w') as f:
        pass

print("Directories and files created successfully!")