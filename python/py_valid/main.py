def valid(s, alphabet):
    """ (str, str) -> bool

    Return True iff s is composed only of characters in alphabet.
    
    >>> valid('adc', 'abcd')
    True
    >>> valid('ABC', 'abcd')
    False
    >>> valid('abc', 'abz')
    False
    """