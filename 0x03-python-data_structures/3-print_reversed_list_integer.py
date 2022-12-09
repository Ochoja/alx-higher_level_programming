#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print list in reverse order
    my_list holds list values
    """
    length = len(my_list) * -1

    for i in range(-1, length, -1):
        print("{}".format(my_list[i]))
