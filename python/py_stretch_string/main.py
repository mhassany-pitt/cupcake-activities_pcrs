def stretch_string(s, stretch_factors):
    """ (str, list of int) -> str

    Precondition: len(s) == len(stretch_factors) and the items of
                  stretch_factors are non-negative
     
    Return a string consisting of the characters in s in the same order as in s,
    repeated the number of times indicated by the item at the corresponding
    position of stretch_factors.
    
    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    # TODO: Replace this comment with the return value of the above function call.
    """