
def can_vote(age):
    """ (int) -> bool

    Return True iff age is legal voting age of at least 18 years.

    >>> can_vote(16)
    False
    >>> can_vote(21)
    True
    """
    
    if age < 18:
        return False
    else:
        return True

    #TODO: Complete the new single-line function body in the space below