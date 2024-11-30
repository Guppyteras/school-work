"""
Assignment 3 File

Full Name: Amedeo Caporuscio
Student Number: 101239905

Please complete the functions based on their definitions and examples
"""

def how_many_vowels(text):
    """
    This function counts the number of vowels in a text. Vowels are the characters a,e,i,o,u and are case insensitive
    
    >>> how_many_vowels("ABC")
    1
    >>> how_many_vowels("aEiO")
    4
    >>> how_many_vowels("TRY")
    0
    >>> how_many_vowels("First Question")
    5
    """
    vowels = set('aeiou')
    text = text.lower(char in vowels for char in text)
    return sum # code goes here. Replace 'pass' with your own python code


def count_whitespaces(text2):
    """
    This function counts the number of whitespaces in a text.

    >>> count_whitespaces("  \t ")  # remember, a tab is 4 white spaces
    6
    >>> count_whitespaces(" Hello World ")
    3
    >>> count_whitespaces("#PythonRules")
    0
    >>> count_whitespaces(" ")
    1
    """
    return sum(1 for char in text2 if char.isspace())  # code goes here. Replace 'pass' with your own python code


def odd_or_even(input):
    """
    This function determines either
    a) if the numerical value is odd or even
    b) if the number of characters of a string is odd or even
    c) if the number of elements in a list or tuple is add or even
    d) If any other data type, there is no return

    >>> odd_or_even("hello world")
    'odd'
    >>> odd_or_even(1234)
    'even'
    >>> odd_or_even(12.34)
    'even'
    >>> odd_or_even(list(range(2, 11)))
    'odd'
    >>> odd_or_even(tuple("cool"))
    'even'
    """
    if isinstance(input, (int, float)):
        return "even" if input % 2 == 0 else "odd"
    elif isinstance(input, (str, list, tuple)):
        return "even" if len(input) % 2 == 0 else "odd"
    else:
        return None  # code goes here. Replace 'pass' with your own python code


def extract_letters(text3):
    """
    Extract all the UNIQUE letters present in the text string.

    >>> extract_letters("Python 123 is C00!_")
    ('p', 'y', 't', 'h', 'o', 'n', 'i', 's', 'c')
    >>> extract_letters("Numbers Are Overrated!")
    ('n', 'u', 'm', 'b', 'e', 'r', 's', 'a', 'o', 'v', 't', 'd')
    >>> extract_letters("123 456")
    ()
    >>> extract_letters("|3 E N!C3")
    ('e', 'n', 'c')

    """
    return tuple(set(char for char in text3 if char.isalpha()))  # code goes here. Replace 'pass' with your own python code


def extract_numbers(text4):
    """
    Extract all the numerical digits in a text string.
    Allow duplicate values as digits.
    Sort the digits in reverse order

    >>> extract_numbers("Python 15-4 is C00!_")
    [5, 4, 1, 0, 0]
    >>> extract_numbers("Sample Param")
    []
    >>> extract_numbers("122333")
    [3, 3, 3, 2, 2, 1]
    >>> extract_numbers("I won 1st prize out of 482 contestants")
    [8, 4, 2, 1]


    """
    digits = [int(digit) for digit in text4 if digit.isdigit()]
    return sorted(digits, reverse=True)  # code goes here. Replace 'pass' with your own python code


def sum_of_odd_numbers(*numbers):
    """
    Write a function that returns the sum of odd numbers
    The function accepts an unlimited about of numerical values
    Assume that there will only be numerical values passed to the function

    Add the necessary parameters to the function definition
    Add a description of the param value
    Add a description of the return value

    >>> sum_of_odd_numbers(1, 3, 5)
    9
    >>> sum_of_odd_numbers(1, 1, 2, 2, 3, 3, 4, 5, 6)
    13
    >>> sum_of_odd_numbers(2, 4, 6, 8, 0, 1)
    1
    >>> sum_of_odd_numbers(1, 2, 3, 4, 5, 6, 7)
    16

    Add 2 more Doctests

    >>
    """
    return sum(num for num in numbers if num % 2 != 0)
  # code goes here. Replace 'pass' with your own python code


def remove_vowels(text5, except_vowels=None):
    """
    This function removes all the vowels in a text and returns a new text without any vowels.
    Vowels are the characters a,e,i,o,u and are case insensitive
    This function allows an optionally tuple data type parameter that represents a series of vowels to except in extraction


    >>> remove_vowels("I like applies")
    ' lk ppls'

    >>> remove_vowels("PYTHON is SUPER cOOl")
    'PYTHN s SPR cl'

    >>> remove_vowels("Are you having fun?", ('a', 'u'))
    'Ar yu havng fun?'

    >>> remove_vowels("Why oh why?", ('o', 'i'))
    'Why oh why?'

    >>> remove_vowels("George Brown College is here for you", ('e'))
    'Gerge Brwn Cllege s here fr y'

    Add 2 more Doctests
	
    """
    except_vowels = except_vowels or []
    vowels = set('aeiou')
    vowels.difference_update(except_vowels)
    return ''.join(char for char in text5 if char.lower() not in vowels)  # code goes here. Replace 'pass' with your own python code

