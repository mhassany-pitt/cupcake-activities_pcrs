
def reorder_by_hashtag(candidate_to_hashtags):
    """(dict of str to list of str) -> dict of str to list of str

    >>> d = reorder_by_hashtag({'Trump':['MakeAmericaGreatAgain', '4Prez'], 'Stein':['4Prez']})
    {'4Prez': ['Stein', 'Trump'], 'MakeAmericaGreatAgain': ['Trump']}
    """