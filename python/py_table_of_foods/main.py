def get_quantities(table_to_foods):
    """ (dict of {str: list of str}) -> dict of {str: int}
	
    The table_to_foods dict has table names as keys (e.g., 't1', 't2', and so on) and each value
    is a list of foods ordered for that table.

    Return a dictionary where each key is a food from table_to_foods and each
    value is the quantity of that food that was ordered.
	
    >>> get_quantities({'t1': ['Vegetarian stew', 'Poutine', 'Vegetarian stew'], 't3': ['Steak pie', 'Poutine', 'Vegetarian stew'], 't4': ['Steak pie', 'Steak pie']})
    {'Vegetarian stew': 3, 'Poutine': 2, 'Steak pie': 3}	
    """

    food_to_quantity = {}

    # Accumulate the food information here.

    return food_to_quantity