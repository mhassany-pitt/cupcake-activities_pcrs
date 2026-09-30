CHILD = "child"
SENIOR = "senior"
ADULT = "adult"

def overdue_fees(days_late, age_group):
    """ (int, str) -> number
    
    Return the fees for a book that is days_late days late for a borrower
    in the age group age_group.
    
    >>> overdue_fees(2, SENIOR) # 2 days late, SENIOR borrower
    0.5
    >>> overdue_fees(5, ADULT) # 5 days late, ADULT borrower
    10
    """