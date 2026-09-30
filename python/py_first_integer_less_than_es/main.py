
def indice_menor(elementos):
    """ (lista de int) -> int
    
    Devuelve el indice del primer entero en elementos que es menor que su indice,
    o -1 si no existe tal entero en elementos.
    
    >>> indice_menor([2, 5, 7, 99, 6])
    -1
    >>> indice_menor([-5, 8, 9, 16])
    0
    >>> indice_menor([5, 8, 9, 0, 1, 3])
    3
    """