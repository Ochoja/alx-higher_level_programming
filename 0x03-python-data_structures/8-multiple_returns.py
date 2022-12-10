#!/usr/bin/python3
def multiple_returns(sentence):
    """
    function returns a tuple with the length of
    a string and its first character
    """
    if sentence == "":
        return None
    else:
        return (len(sentence), sentence[0])
