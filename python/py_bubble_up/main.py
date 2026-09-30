
def bubble_up(L, start, end):
    """ (list, int, int) -> NoneType

    Bubble up through L[start:end], swapping items that are out of order.

    >>> L = [4, 3, 2, 1, 0]
    >>> bubble_up(L, 0, 3)
    >>> L
    [3, 2, 1, 4, 0]
    >>> L = [4, 3, 2, 1, 0]
    >>> bubble_up(L, 2, 4)
    >>> L
    [4, 3, 1, 0, 2]
    """

    for i in range(start, end):
        if L[i] > L[i + 1]:
            L[i], L[i + 1] = L[i + 1], L[i]

def bubble_down(L, start, end):
    """ (list, int, int) -> NoneType

    Bubble down through L from indexes end through start, swapping items that are out of place.

    >>> L = [4, 3, 2, 1, 0]
    >>> bubble_down(L, 1, 3)
    >>> L
    [4, 1, 3, 2, 0]
    """