#!/usr/bin/python3
def multiple_returns(sentence):
    """My function returns a tuple with the length of
    a string and its first character.

    Arg:

    sentence: parameter string

    Return:

    return tuple of two elements
    """
    if len(sentence) == 0:
        return None
    return tuple(len(sentence), sentence[0])
