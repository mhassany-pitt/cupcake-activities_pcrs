def busqueda_inversa_listas(num_telefono, numeros_telefono, nombres):
    """ (str, lista de str, lista de str) -> str

    Precondicion: len(numeros_telefono) == len(nombres)

    Esta funcion recibe un numero de telefono num_telefono, y dos listas: una lista de 
    numeros de telefono numeros_telefono y una lista de nombres nombres. Estas listas son
    listas paralelas, por lo que el nombre en la posicion 0 de la lista de nombres esta 
    asociado con el numero de telefono en la posicion 0 de la lista numeros_telefono, y asi sucesivamente.

    Devuelve el nombre asociado con num_telefono segun numeros_telefono
    y nombres, o un string vacia si no hay coincidencia.
    
    >>> busqueda_inversa_listas('416-555-6543', ['416-555-3498', \\
        '647-555-9812', '416-555-6543', '905-555-6681'], ['John A. Macdonald', \\
        'Louis Riel', 'Canoe Head', 'Tim Horton'])        
    'Canoe Head'
    """