#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints x elements in a list
    """
    num_printed = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            num_printed += 1
        except IndexError:
            break

    return num_printed