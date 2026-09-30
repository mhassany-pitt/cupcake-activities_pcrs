def is_correct(dictionary, word):
    """ (Open File for reading, str) -> bool
    
    Return True iff word is a correctly-spelled word in dictionary.
    
    >>> dict1 = open('dict.txt', 'r')
    >>> is_correct(dict1, "Zyrtec")
    True
    >>> dict1.close()

    >>> dict1 = open('dict.txt', 'r')
    >>> is_correct(dict1, "lolz")
    False
    >>> dict1.close()
    """