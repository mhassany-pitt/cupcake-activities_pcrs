def estirar_string(c, factores_estiramiento):
    """ (str, lista de int) -> str

    Precondicion: len(c) == len(factores_estiramiento) y los elementos de
                  factores_estiramiento son mayores o iguales a cero
     
    Devuelve una  string que consiste en los caracteres en c en el mismo orden que en c,
    repetidos el numero de veces indicado por el elemento en la posicion correspondiente
    de factores_estiramiento.
    
    >>> estirar_string('Hola', [2, 0, 3, 1])
    'HHllla'
    >>> estirar_string('eco', [0, 1, 2])
    #TODO: Reemplaza este comentario con el valor de retorno de la llamada a la funcion anterior.
    """