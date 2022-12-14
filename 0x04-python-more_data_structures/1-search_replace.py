#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search_replace- replace all occurence of an element by another
    @my_list: the initial list
    @search: is the element to replace in the list
    @replace is the new element
    """
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if search == new_list[i]:
            new_list[i] = replace

    return new_list
