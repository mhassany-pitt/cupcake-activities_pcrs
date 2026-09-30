
class Rectangulo:
    """ Un rectangulo con un ancho y altura. """

    def __init__(self, an, al):
        """ (Rectangulo, numero, numero)

        Crea un nuevo rectangulo de ancho a y altura h.

        >>> r = Rectangulo(1, 2)
        >>> r.ancho
        1
        >>> r.altura
        2
        """

        self.ancho = an
        self.altura = al

    def area(self):
        """ (Rectangulo) -> numero

        Devuelve el area de este rectangulo.

        >>> r = Rectangulo(10, 20)
        >>> r.area()
        200
        """