def buscar_armario(elementos, color):
    """ (lista de str, str) -> lista de str
    
    elementos es una lista que contiene descripciones del contenido de un armario donde
    cada descripcion tiene la forma 'color articulo', donde cada color es una palabra
    y cada articulo es una o mas palabras. Por ejemplo:

        ['gris chaqueta de verano', 'naranja chaqueta de primavera', 'rojo zapatos', 'verde sombrero']

    color es un color que se esta buscando en elementos. 
    
    Devuelve una lista que contiene solo los articulos que coinciden con el color.
    
    >>> buscar_armario(['rojo chaqueta de verano', 'naranja chaqueta de primavera', 'rojo zapatos', 'verde sombrero'], 'rojo')
    ['rojo chaqueta de verano', 'rojo zapatos']
    >>> buscar_armario(['rojo camisa', 'verde pantalones'], 'azul')
    []
    >>> buscar_armario([], 'malva')
    []
    """