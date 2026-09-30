
def valid_DNA_sequence(sequence, DNA_alphabet):
    """ (str, str) -> bool
    
    Return True iff sequence is composed only of characters found in DNA_alphabet.

    >>> valid_DNA_sequence('AmGTCA', 'ACGT')
    False
    >>> valid_DNA_sequence('AmGTCA', 'ACGTmh')
    True
    """
