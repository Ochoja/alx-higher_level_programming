#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add values in tuples eg.
    element 1 in tuple_a is added to
    element 1 in tuple_b
    """
    if tuple_a == ():
        return tuple_b
    elif tuple_b == ():
        return tuple_a

    new_tuple = ()

    if len(tuple_a) > len(tuple_b):
        for i in range(len(tuple_b)):
            temp = (tuple_a[i] + tuple_b[i],)
            new_tuple += temp
        new_tuple += tuple_a[i+1:]
    else:
        for i in range(len(tuple_a)):
            temp = (tuple_a[i] + tuple_b[i],)
            new_tuple += temp
    return new_tuple
