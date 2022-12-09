#!/usr/bin/python3
def no_c(my_string):
    """
    removes all characters 'c'
    and 'C' from a string
    """

    for i in range(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string.pop(i)
