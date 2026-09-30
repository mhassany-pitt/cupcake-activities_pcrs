
def ticket_price(age):
    """ (int) -> float
    
    Precondition: age > 0
    
    Return the ticket price for a person with age in years. Seniors 65 and over
    pay 4.75, kids 12 and under pay 4.25, and everyone else pays 7.50.

    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75
    """