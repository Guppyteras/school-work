# Create a function that
# has two parameters
# creates and returns a tuple of the two function arguments
def create_tuple(arg1, arg2):
    # Create a tuple of the two function arguments
    tup = (arg1, arg2)
    # Return the tuple
    return tup

# Call and output the result of the function above with any two arguments
args = ('apple', 5)
print("Function arguments as a tuple:", create_tuple(*args))