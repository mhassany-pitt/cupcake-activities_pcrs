
def primera_diferencia(lista1, lista2):
    """ (list, list) -> int
    
    Devuelve el primer indice en el que los valores de lista1 y lista2 difieren. 
    Devuelve -1 si no se encuentran diferencias.
       
    >>> primera_diferencia(['a', 'b', 'c'], ['a', 'd', 'c'])
    1
    >>> primera_diferencia(['a', 'b', 'c'], ['a', 'b', 'c', 'd'])
    3
    >>> primera_diferencia(['a', 'b', [1]], ['a', 'b', [1]])
    -1
    """