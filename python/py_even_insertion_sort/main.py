
def insert_even(L, i):
    """ (list, int) -> NoneType

    Precondition: L[:i] is sorted on the even indices from smallest to largest.

    Move L[i] to where it belongs in L[:i + 2].

    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [5, 3, 7, 2]
    """