#!/usr/bin/python3
"""
    5-text_indentation: text_indentation()
"""


def text_indentation(text):
   """ Text indentation function
   Args:
        text (str): A string of text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    no_spaces = True
    size = 0
    text = text.strip()
    new_text = ""
    for t in text:
        if t is " " and no_space:
            pass
        elif t is "." or t is "?" or t is ":":
            new_text += t + "\n\n"
            no_spaces = True
        else:
            new_text += x
            no_spaces = False
    print(new_text, end='')