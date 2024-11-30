def get_data_types(*args):
    """
    This function takes any number of arguments and returns a list of the data types of the arguments as strings.

    Example:
        get_data_types(1, "hi", 1.1) -> ['int', 'string', 'float']

    Parameters:
        *args: Variable length argument list

    Returns:
        A list of the data types of the input arguments as strings.
    """
    return [type(arg).__name__ for arg in args]

def repeat_text(text, num):
    """
    This function takes a string and a number, and checks if both parameters are the specified data types and if the number is at least 2.
    If the verification fails, it returns False. Otherwise, it returns a string that repeats the text X times (value of the second argument).

    Parameters:
        text (str): The text to be repeated.
        num (int): The number of times the text should be repeated.

    Returns:
        A string that contains the input text repeated N times.
    """
    if not isinstance(text, str) or not isinstance(num, int) or num < 2:
        return False
    return text * num

def print_first_name():
    """
This function takes no arguments and prints the first name of the user.
It returns the last name.
"""
    first_name = "John"
    print(first_name)
    return "Doe"

def is_factor(num1, num2):
    """
    This function takes two numbers and returns True if the first number is a factor of the second number.

    Parameters:
        num1 (int): The first number to be checked.
        num2 (int): The second number.

    Returns:
        A boolean value indicating if the first number is a factor of the second number.
    """
    return num1 and num2 and num2 % num1 == 0

def is_valid_postal_code(postal_code):
    """
    This function takes a string and returns True if it is a valid Canadian postal code.

    Parameters:
        postal_code (str): The postal code to be checked.

    Returns:
        A boolean value indicating if the input is a valid Canadian postal code.
    """
    return len(postal_code) == 6 and postal_code.isalpha()

def format_name(first_name, last_name):
    """
    This function takes a first and last name and returns a string that contains the last name, followed by a comma, and then the first name.

    Parameters:
        first_name (str): The first name.
        last_name (str): The last name.

    Returns:
        A string that contains the last name, followed by a comma, and then the first name.
    """
    return f"{last_name}, {first_name}"

if __name__ == '__main__':
    # Task 1
    print(get_data_types(1, "hi", 1.1))
    print(get_data_types(1, 2, 3))
    print(get_data_types("hi", "there", "friend"))

    # Task 2
    print(repeat_text("Hello", -2))
    print(repeat_text("World", 5))
    print(repeat_text("False", 1))
    print(repeat_text("True", 3))

    # Task 3
    print(print_first_name())

    # Task 4
    print(is_factor(2, 4))
    print(is_factor(3, 10))

    # Task 5
    print(is_valid_postal_code("A1A 1A1"))
    print(is_valid_postal_code("A1A1A1"))

    # Task 6
    print(format_name("John", "Doe"))
    print(format_name("Jane", "Smith"))

# Task 8
"""
Test functions 1-7
"""
import doctest

def test_func():
    """
    Test functions 1-7
    """
    return doct