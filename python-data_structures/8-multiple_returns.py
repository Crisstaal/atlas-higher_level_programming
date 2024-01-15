#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentence)
    if (len == 0):
        new_tuple = (len(str(None)), )
    else:
        new_tuple = (len, sentence[0])
        return (new_tuple)
