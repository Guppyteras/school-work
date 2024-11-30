import os

new_dir_path = 'new_directory'
new_dir_path_recursive = 'data/temp/new_directory'

# Using os.mkdir() to create a new directory
if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)
    print("Folder %s created!" % new_dir_path)
else:
    print("Folder %s already exists" % new_dir_path)

# Using os.makedirs() to create a new directory recursively
if not os.path.exists(new_dir_path_recursive):
    os.makedirs(new_dir_path_recursive)
    print("Folder %s created!" % new_dir_path_recursive)
else:
    print("Folder %s already exists" % new_dir_path_recursive)