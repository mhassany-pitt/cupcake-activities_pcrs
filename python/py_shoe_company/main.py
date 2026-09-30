
def build_placements(shoes):
    """ (list of str) -> dict of {str: list of int}

    Return a dictionary where each key is a shoe company from shoes and each value is a
    list of placements by people wearing footwear made by that company. First place is at index
    0 of shoes, 2nd place is at index 1, and so on.

    >>> build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
                          'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    {'Saucony': [1, 5, 9] 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}                      
    """