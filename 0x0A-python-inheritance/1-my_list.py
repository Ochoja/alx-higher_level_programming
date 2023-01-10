#!/usr/bin/python3
"""
contains custom list class
"""


class MyList(list):
    """custom list class that"""
    def print_sorted(self):
        """prints list in ascending order"""
        new_list = list(eval(repr(self)))
        new_list.sort()
        print(new_list)

    def append(self, item):
        if not isinstance(item, int):
            raise ValueError("list must contain integers only")
        super().append(item)
