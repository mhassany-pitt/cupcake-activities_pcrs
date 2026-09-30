
def smaller_index(items):
    """ (list of int) -> int
    
    Return the index of the first integer in items that is less than its index,
    or -1 if no such integer exists in items.
    
    >>> smaller_index([2, 5, 7, 99, 6])
    -1
    >>> smaller_index([-5, 8, 9, 16])
    0
    >>> smaller_index([5, 8, 9, 0, 1, 3])
    3
    """