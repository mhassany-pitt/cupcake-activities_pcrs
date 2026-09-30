def insert(lst, v):
    """ (list of int, int) -> NoneType

    Insert v into lst just before the rightmost item greater than v, or at
    index 0 if no items are greater than v.

    >>> my_list = [3, 10, 4, 2]
    >>> insert(my_list, 5)
    >>> my_list
    [3, 5, 10, 4, 2]
    >>> my_list = [5, 4, 2, 10]
    >>> insert(my_list, 20)
    >>> my_list
    [20, 5, 4, 2, 10]
    """