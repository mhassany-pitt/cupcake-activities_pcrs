def get_lines(f):
    """ (file open for reading) -> list of str"""
    result = []
    for line in f:
        result.append(line.strip())
    return result