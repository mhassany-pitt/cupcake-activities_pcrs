
def insertar(lista, v):
    """ (lista de int, int) -> NoneType

    Insertar v en lista justo antes del ultimo elemento mayor que v, o en
    el indice 0 si ningun elemento es mayor que v.

    >>> mi_lista = [3, 10, 4, 2]
    >>> insertar(mi_lista, 5)
    >>> mi_lista
    [3, 5, 10, 4, 2]
    >>> mi_lista = [5, 4, 2, 10]
    >>> insertar(mi_lista, 20)
    >>> mi_lista
    [20, 5, 4, 2, 10]
    """