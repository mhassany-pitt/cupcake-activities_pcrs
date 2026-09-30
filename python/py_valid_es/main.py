def valido(string, alfabeto):
    """ (str, str) -> bool

    Devolver True si y solo si string esta compuesta solo de caracteres en alfabeto.
    
    >>> valido('adc', 'abcd')
    True
    >>> valido('ABC', 'abcd')
    False
    >>> valido('abc', 'abz')
    False
    """