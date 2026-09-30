def formato_nombre(primero, ultimo):
    """ (str, str) -> str
    
    Devuelve el nombre y apellido dados como un unico string, en la forma:
    APELLIDO, NOMBRE
    donde APELLIDO y NOMBRE son reemplazados por ultimo y primero.
    Las personas mononimas (aquellas sin apellido) deben tener su nombre
    devuelto sin una coma.

    >>> formato_nombre('Cherilyn', 'Sarkisian')
    'Sarkisian, Cherilyn' 
    >>> formato_nombre('Cher', '')
    'Cher'
    """