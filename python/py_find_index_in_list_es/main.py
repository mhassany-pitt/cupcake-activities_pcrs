def encontrar_valor_en_indices(lista_de_items, lista_de_indices, v):
    """ (lista de objeto, lista de int, objeto) -> lista de int

    Precondicion: los valores en lista_de_indices son indices validos en lista_de_items.

    v puede aparecer multiples veces en lista_de_items. lista_de_indices contiene cero o
    mas indices. Devuelve una lista de los indices de lista_de_indices en los que v
    aparece en lista_de_items.

    >>> encontrar_valor_en_indices([6, 8, 8, 5, 8], [0, 2, 4], 8)
    [2, 4]
    """