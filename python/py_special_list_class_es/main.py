
class ListaEspecial:
    """Una lista que puede contener un numero limitado de elementos."""

    def __init__(self, tamano):
        """ (ListaEspecial, int)

        >>> L = ListaEspecial(10)
        >>> L.tamano
        10
        >>> L.lista_valores
        []
        """
        # complete este codigo


    def agregar_valor(self, nuevo_valor):
        """ (ListaEspecial, object) -> NoneType

        Agregar nuevo_valor a esta lista, si hay suficiente espacio en la lista segun su tamano maximo.
        Si no hay espacio suficiente, nuevo_valor no debe ser agregado a la lista.

        >>> L = ListaEspecial(10)
        >>> L.agregar_valor(3)
        >>> L.lista_valores
        [3]
        """
        # complete este codigo


    def eliminar_valor_mas_reciente(self):
        """ (ListaEspecial) -> object

        Precondicion: len(self.lista_valores) != 0

        Retornar el valor agregado mas recientemente a lista_valores y eliminarlo de la lista.

        >>> L = ListaEspecial(10)
        >>> L.agregar_valor(3)
        >>> L.agregar_valor(4)
        >>> L.lista_valores
        [3, 4]
        >>> L.eliminar_valor_mas_reciente()
        4
        """
        # complete este codigo

    
    def comparar(self, otro):
        """ (ListaEspecial, ListaEspecial) -> int

        Retornar 0 si ambos objetos ListaEspecial tienen listas que contienen el mismo numero de elementos.
        Retornar 1 si la lista de self contiene mas elementos que la lista de otro.
        Retornar -1 si la lista de self contiene menos elementos que la lista de otro.
        """
        # complete este codigo