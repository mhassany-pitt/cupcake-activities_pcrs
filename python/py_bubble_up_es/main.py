
def burbujear_hacia_arriba(L, inicio, fin):
    """ (list, int, int) -> NoneType

    Burbujear hacia arriba a traves de L[inicio:fin], intercambiando elementos que estan fuera de orden.

    >>> L = [4, 3, 2, 1, 0]
    >>> burbujear_hacia_arriba(L, 0, 3)
    >>> L
    [3, 2, 1, 4, 0]
    >>> L = [4, 3, 2, 1, 0]
    >>> burbujear_hacia_arriba(L, 2, 4)
    >>> L
    [4, 3, 1, 0, 2]
    """

    for i in range(inicio, fin):
        if L[i] > L[i + 1]:
            L[i], L[i + 1] = L[i + 1], L[i]

def burbujear_hacia_abajo(L, inicio, fin):
    """ (list, int, int) -> NoneType

    Burbujear hacia abajo a traves de L desde los indices fin hasta inicio, intercambiando elementos que estan fuera de lugar.

    >>> L = [4, 3, 2, 1, 0]
    >>> burbujear_hacia_abajo(L, 1, 3)
    >>> L
    [4, 1, 3, 2, 0]
    """