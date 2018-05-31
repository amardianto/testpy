def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # The convention followed for a docstring is a multi-line string where the first line starts with a capital letter and ends with a dot. 
    # Then the second line is blank followed by any detailed explanation starting from the third line.
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(7, 5)
print(print_max.__doc__)
