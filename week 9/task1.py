import re

# Task 1
text = " "
number = 1000
username = "admin"
userid = 12345
password = "a8e3l6$#"
email = "ex@ex.ex"

# Task 2
empty_string_regex = re.compile(r'^$')

# Task 3
min_10_chars_regex = re.compile(r'^.{10,}$')

# Task 4
only_non_alnum_regex = re.compile(r'^[^a-zA-Z0-9]*$')

# Task 5
only_alpha_underscore_regex = re.compile(r'^[a-zA-Z_]*$')

# Task 6
only_numbers_regex = re.compile(r'^[0-9]*$')

# Task 7
valid_password_regex = re.compile(r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*/]).*$')

# Task 8
valid_email_regex = re.compile(r'^[a-zA-Z]+[a-zA-Z0-9]*@[a-zA-Z]+[a-zA-Z0-9]*\.[a-zA-Z]{2,}$')

# Testing
print("Empty String:", bool(empty_string_regex.match(text)))
print("Min 10 Chars:", bool(min_10_chars_regex.match(text)))
print("Only Non-Alnum:", bool(only_non_alnum_regex.match(text)))
print("Only Alpha Underscore:", bool(only_alpha_underscore_regex.match(username)))
print("Only Numbers:", bool(only_numbers_regex.match(str(userid))))
print("Valid Password:", bool(valid_password_regex.match(password)))
print("Valid Email:", bool(valid_email_regex.match(email)))