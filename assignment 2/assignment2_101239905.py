"""
Assignment 2 File

Full Name: Amedeo Caporuscio
Student Number: 101239905

Only edit the text where indicated
Make sure that the final result of the function is stored in the variable RESULT
"""


def task1(salary):
    """
    Given the Federal Income Tax Rates chart located below,

    Tax rate	Taxable income threshold
    15%	        $55,000 or less
    21%	        $55,001 up to $111,000
    26%	        $111,001 up to $173,000
    29%	        $173,001 up to $246,000
    33%	        $246,001 or higher

    Code the function that accepts ONE gross salary and returns net salary and tax rate as a string percent as a tuple:

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: The method can accept string and int values (no float values)
    NOTE: the salary will only accept whole values for the gross salary value
    NOTE: the net value should be rounded to the nearest whole number. Remove all decimal values
    NOTE: error handling is not expected of you, assume that if the value passed is a string value, all characters will be 0-9
    >>> task1(100000)
    (79000, '21%')
    >>> task1(180000)
    (127800, '29%')
    >>> task1(250000)
    (167500, '33%')
    >>> task1('23456')
    (19938, '15%')
    >>> task1('55000')
    (46750, '15%')
    """
    ########################
    # Start writing code
    ########################
    # Convert the salary to an integer if it's a string
    if isinstance(salary, str):
        salary = int(salary)

    # Define the tax brackets
    tax_brackets = [(55000, 15), (111000, 21), (173000, 26), (246000, 29), (float('inf'), 33)]

    # Find the tax bracket that the salary falls into
    for i in range(len(tax_brackets)):
        if salary <= tax_brackets[i][0]:
            tax_rate = tax_brackets[i][1]
            taxable_income_threshold = tax_brackets[i][0]
            break

    # Calculate the tax amount
    tax_amount = (salary - taxable_income_threshold) * (tax_rate / 100)

    # Calculate the net salary
    net_salary = salary - tax_amount

    # Round the net salary to the nearest whole number
    net_salary = round(net_salary)

    # Return the net salary and tax rate as a tuple
    return (net_salary, f'{tax_rate}%')
    ########################
    # End writing code
    ########################


def task2(monthly_budget, max_expense, expenses):
    """
    Code a function that accepts
        1) Accept a monthly budget value
        2) A maximum expense value
        3) A dictionary of expenses with the folllowing keys-value pair
            key = expense name: string value
            value = expense price: int/float value
            
        Iterate the dictionary of values and return one of the following values
            True & sum of all expenses: if the sum of all expenses is less than or equal to the monthly budget value
            False & sum of all expenses: if the sum of all expenses is greater than the monthly budget value
            False, the expense name & the expense value of the FIRST expense that is greater than the maximum expense value

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: error handling is not expected of you, assume that if the values passed will be int, int and dictionary

    >>> task2(100, 40, {'food': 20, 'fun': 15, 'clothes': 30, 'travel': 25})
    (True, 90)
    >>> task2(150, 35, {'food': 30, 'books': 35, 'internet': 40, 'streaming services': 15})
    (False, 'internet', 40)
    >>> task2(180, 40, {'food': 30, 'fun': 25, 'clothes': 30, 'travel': 25, 'books': 35, 'internet': 40, 'streaming services': 15})
    (False, 200)
    >>> task2(300, 50, {'coat': 30, 'jeans': 20, 'hat': 15, 'scarf': 10, 'boots': 40, 'socks': 5, 'food': 20, 'fun': 15, 'clothes': 30, 'travel': 25})
    (True, 210)
    >>> task2(500, 100, {'coffee': 40, 'restaurant': 200, 'travel': 50, 'plan ticket': 350, 'school': 90})
    (False, 'restaurant', 200)
    """
    ########################
    # Start writing code
    ########################
    pass
    # Initialize variables
    expense_sum = 0
    max_expense_exceeded = None

    # Iterate over the dictionary of expenses
    for expense_name, expense_price in expenses.items():
        # Add the expense price to the sum of all expenses
        expense_sum += expense_price

        # Check if the expense price is greater than the maximum expense
        if expense_price > max_expense:
            # If it is, update the max_expense_exceeded variable
            max_expense_exceeded = (expense_name, expense_price)

    # Check if the sum of all expenses is greater than the monthly budget
    if expense_sum > monthly_budget:
        # If it is, return False, the sum of all expenses, and the max expense exceeded
        return False, expense_sum, max_expense_exceeded

    # If the sum of all expenses is less than or equal to the monthly budget, return True and the sum of all expenses
    return True, expense_sum
    ########################
    # End writing code
    ########################



def task3(data):
    """
    This function accepts one parameter returns either 'odd', 'even' or None.
    The function determines whether or not
        a) if the numerical value is odd or even
        b) if the number of characters of a string is odd or even
        c) if the number of elements in a list, set or tuple is add or even
        d) If any other data type, there is no return

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: you are expected to determine the data type of the parameter and return the appropriate string value


    >>> task3("hello world")
    'odd'
    >>> task3(1234)
    'even'
    >>> task3({1,1,2,3,4,5,2,3,4,5,6})
    'even'
    >>> task3(list(range(2, 11)))
    'odd'
    >>> task3(tuple("cool"))
    'even'
    """
    ########################
    # Start writing code
    ########################
    pass
# Check the data type of the input parameter
    if isinstance(data, int):
        # For integer data type, check if it's odd or even
        return 'odd' if data % 2 != 0 else 'even'
    elif isinstance(data, str):
        # For string data type, check if the number of characters is odd or even
        return 'odd' if len(data) % 2 != 0 else 'even'
    elif isinstance(data, (list, tuple, set)):
        # For list, tuple, or set data types, check if the number of elements is odd or even
        return 'odd' if len(data) % 2 != 0 else 'even'
    else:
        # For other data types, return None
        return None

    ########################
    # End writing code
    ########################
