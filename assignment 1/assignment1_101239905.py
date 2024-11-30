"""
Assignment 1 File

Full Name: Amedeo Caporuscio
Student Number: 101239905

Only edit the text where indicated
Make sure that the final result of the function is stored in the variable RESULT
"""


def task1(text1, text2, text3):
    """
    returns the text that is the longest. if there is a tie, concatenate the text(s), seperated by underscores in same order of the arguments


    >>> task1("hi", "bye", "hello")
    'hello'
    >>> task1("hello", "create", "every")
    'create'
    >>> task1("hi", "al", "oh")
    'hi_all_oh'
    >>> task1("two", "hi", "one")
    'two_one'
    >>> task1(" ", "  ", "   ")
    '   '


    """
    result = ''
    ########################
    # Start writing code
    ########################
    # Compare lengths of texts
    max_length = max(len(text1), len(text2), len(text3))

    # Check which text(s) have the maximum length
    if len(text1) == max_length:
        result += text1
    if len(text2) == max_length:
        if result:
            result += '_'
        result += text2
    if len(text3) == max_length:
        if result:
            result += '_'
        result += text3

    
    ########################
    # End writing code
    ########################
    return result


def task2(operand1, operator, operand2):
    """
    returns the result or an arithmetic operation. Accept the following four operators +, -, * & /.

    >>> task2(10, "+", 5)
    15
    >>> task2(10, "-", 5)
    5
    >>> task2("10", "*", 5)
    50
    >>> task2("10", "/", "5")
    2
    >>> task2("5", "-", 10)
    -5



    """
    result = ''
    ########################
    # Start writing code
    ########################
    # Convert operands to float for numeric operations
    operand1 = float(operand1)
    operand2 = float(operand2)

    # Perform arithmetic operations based on the operator
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        # Check for division by zero
        if operand2 != 0:
            result = operand1 / operand2
        else:
            result = "Error: Division by zero"
    ########################
    # End writing code
    ########################
    return result


def task3(name):
    """
    Determines if name is valid. A valid name contains at one and only one space and at least 5 characters
    >>> task3("foo")
    False
    >>> task3("having fun?")
    True
    >>> task3("Python Rocks")
    True
    >>> task3("Python is the best language")
    False
    >>> task3("a b")
    False

    """
    result = ''
    ########################
    # Start writing code
    ########################
    # Check if the name has at least 5 characters and contains one and only one space
    if len(name) >= 5 and name.count(' ') == 1:
        result = True
    ########################
    # End writing code
    ########################
    return result


def task4(value, multiplier):
    """
    returns either a string repeated X times or the product of two numbers (the arithmetic operation). Return False if second argument is NOT a number
    >>> task4("hello", 3)
    'hellohellohello'
    >>> task4(10, 3)
    30
    >>> task4('10', 3)
    '101010'
    >>> task4('10', '3')
    False
    >>> task4('hi', '2')
    False


    """
    result = ''
    ########################
    # Start writing code
    ########################
  # Check if the second argument is a number
    if isinstance(multiplier, (int, float)):
        # Check if the first argument is a string, then repeat it, or perform multiplication
        if isinstance(value, str):
            result = value * int(multiplier)
        else:
            result = value * multiplier

    ########################
    # End writing code
    ########################
    return result

