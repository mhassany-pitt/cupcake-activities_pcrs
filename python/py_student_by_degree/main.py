def students_by_degree(student_list, degree_type):
    """ (list of str, str) -> list of str

    Return a list of the elements of student_list which are enrolling in the degree_type in the order
    they appear in the original list.

    >>> students_by_degree(['Jacqueline Smith,Best High School,2002,MAT,90,94,ENG,92,88,CHM,80,85,BArts',
                           'Paul Gries,Another High School,1990,BIO,60,70,CHM,80,90,CAT,95,96,BEng',
                           'Jen Campbell,Yet Another High School,2015,ENG,75,78,SCI,80,81,CHM,80,81,BEng'],
                           'BEng')
    ['Paul Gries,Another High School,1990,BIO,60,70,CHM,80,90,CAT,95,96,BEng', 'Jen Campbell,Yet Another High School,2015,ENG,75,78,SCI,80,81,CHM,80,81,BEng']
    """
