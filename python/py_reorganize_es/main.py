def reorganizar(orig_dicc):
    """ (dict de str a lista de str) -> dict de str a lista de str
    
    >>> reorganizar({'Clave1':["string1", "string2"], 'Clave2':["string2"]})
    {'string1':['Clave1'], 'string2':['Clave1', 'Clave2']}
    """