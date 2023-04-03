#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines
    after '.', '?' or ':' characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print("{}\n\n".format(text[i]), end="")
        elif text[i - 1] in ['.', '?', ':'] and text[i] == ' ':
            continue
        else:
            print(text[i], end="")
