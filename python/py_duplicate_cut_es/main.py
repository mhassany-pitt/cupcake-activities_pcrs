def corte_duplicado(lista_enzimas):
    """ (lista de str) -> booleano

    Devuelve True si y solo si la misma enzima esta en la lista de enzimas en posiciones adyacentes.

    >>> corte_duplicado(['EcoRI', 'Sau3A', 'Sau3A'])
    True
    >>> corte_duplicado(['EcoRI', 'Sau3A', 'EcoRI'])
    False
    """