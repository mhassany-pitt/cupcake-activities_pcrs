
def is_teenager(age):
    """ (int) -> bool

    Return True iff age represents a teenager between 13 and 18 inclusive.

    >>> is_teenager(4)
    False
    >>> is_teenager(16)
    True
    >>> is_teenager(19)
    False
    """

    if age < 13:
        return False
    else:
        if age > 18:
            return False
        else:
            return True

    #TODO: complete the new single-line function body in the space below: