# Create a dictionary of 3 key-value pairs
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# GET the value of one of the keys
value = my_dict['key1']

# Remove one of the keys
del my_dict['key1']

# Output the dictionary using a loop in the format of key = value python
for key, value in my_dict.items():
    print(f"{key} = {value}")