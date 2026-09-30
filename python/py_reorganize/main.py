def reorganize(orig_dict):
    """ (dict of str to list of str) -> dict of str to list of str
    
    >>> reorganize({'Key1':["str1", "str2"], 'Key2':["str2"]})
    {'str1':['Key1'], 'str2':['Key1', 'Key2']}
    """