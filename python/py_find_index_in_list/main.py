def find_value_indexes(item_list, index_list, v):
    """ (list of object, list of int, object) -> list of int

    Precondition: the values in index_list are valid indexes in item_list.

    v may appear multiple times in item_list.  index_list contains zero or
    more indexes.  Return a list of the indexes from index_list at which v
    appears in item_list.

    >>> find_value_indexes([6, 8, 8, 5, 8], [0, 2, 4], 8)
    [2, 4]
    """