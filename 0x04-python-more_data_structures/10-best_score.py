#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value
    """
    if a_dictionary:
        first_key = list(a_dictionary.keys())[0]
        biggest = a_dictionary[first_key]
        big_key = first_key

        for key in a_dictionary:
            if a_dictionary[key] >= biggest:
                biggest = a_dictionary[key]
                big_key = key

        return big_key
    else:
        return None
