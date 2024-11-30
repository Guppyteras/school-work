# Write a function that
# has 1 parameter (assume that it is a string)
# returns the first character and the last character of the string
def first_last_char(s):
    # Return the first and last character of the string
    return s[0], s[-1]

# Call and output the result of the function above with a string argument
print("First and last character of the string:", first_last_char('hello'))