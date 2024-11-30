def task1(text1, text2, text3):
    """
    returns the text that is the longest. if there is a tie, concatenate the text(s), separated by underscores in the same order of the arguments

    >>> task1("hi", "bye", "hello")
    'hello'
    >>> task1("hello", "create", "every")
    'create'
    >>> task1("hi", "al", "oh")
    'hi_al_oh'
    >>> task1("two", "hi", "one")
    'two_one'
    >>> task1(" ", "  ", "   ")
    '   '
    """
    result = ''

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

    return result

# Testing the function
print(task1("hi", "bye", "hello"))
print(task1("hello", "create", "every"))
print(task1("hi", "al", "oh"))
print(task1("two", "hi", "one"))
print(task1(" ", "  ", "   "))