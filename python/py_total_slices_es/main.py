def total_slices(num_pizzas, slices_per_pizza):
    """ (int, int) -> int

    Return the total number of slices in num_pizzas pizzas that each have
    slices_per_pizza slices.
    
    >>> total_slices(2, 30)
    60
    >>> total_slices(1, 8)
    8
    """
    
    return num_pizzas * slices_per_pizza


# We ordered 2 medium pizzas.
medium_slices = total_slices(2, 8)

# We also ordered 1 extra large pizza.
pieces_per_extra_large = 30
extra_large_slices = total_slices(1, pieces_per_extra_large)

grand_total = medium_slices + extra_large_slices

print("With 2 mediums and 1 extra large, we will have", grand_total, "slices.")
