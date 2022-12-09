#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    function replaces an element in a list
    at a specific position without modifying
    the original list, idx holds index, element
    holds index value
    """
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
