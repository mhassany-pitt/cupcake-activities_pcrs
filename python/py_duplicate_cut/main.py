
def duplicate_cut(enzyme_list):
    """ (list of str) -> bool

    Return True iff the same enzyme is in the enzyme list in adjacent positions.

    >>> duplicate_cut(['EcoRI', 'Sau3A', 'Sau3A'])
    True
    >>> duplicate_cut(['EcoRI', 'Sau3A', 'EcoRI'])
    False
    """