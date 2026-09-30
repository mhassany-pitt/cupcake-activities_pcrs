def first_mismatch(lst1, lst2):
    """ (list, list) -> int
    
    Return the first index at which the values of lst1 and lst2 differ. 
    Return -1 if no differences are found.
       
    >>> first_mismatch(['a', 'b', 'c'], ['a', 'd', 'c'])
    1
    >>> first_mismatch(['a', 'b', 'c'], ['a', 'b', 'c', 'd'])
    3
    >>> first_mismatch(['a', 'b', [1]], ['a', 'b', [1]])
    -1
    """