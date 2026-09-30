
def encontrar_letra_n_veces(string, letra, n):
    """ (str, str, int) -> str

    Precondicion: 'letra' ocurre al menos 'n' veces en 'string'

    Devuelve el substring mas pequeno de 'string' comenzando desde el indice 0 que contiene
    n ocurrencias de 'letra'.

    >>> encontrar_letra_n_veces('Ciencias de la Computacion', 'e', 2)
    'Ciencias de'
    """

    i = 0
    cuenta = 0
    
    #TODO completa el resto de la funcion abajo