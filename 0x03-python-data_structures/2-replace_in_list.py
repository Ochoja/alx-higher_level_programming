#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    my_list takes list argument, idx
    refers holds index value, element
    value replaces value at index
    """

    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
