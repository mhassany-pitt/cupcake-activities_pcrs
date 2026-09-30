class Rectangulo:
    """ Un rectangulo con un ancho y alto. """

    def __init__(self, an, al):
        """ (Rectangulo, numero, numero)

        Crea un nuevo rectangulo de ancho an y alto al.

        >>> r = Rectangulo(1, 2)
        >>> r.ancho
        1
        >>> r.alto
        2
        """

        self.ancho = an
        self.alto = al

    def obtener_area(self):
        """ (Rectangulo) -> numero

        Devuelve el area de este rectangulo.

        >>> r = Rectangulo(10, 20)
        >>> r.obtener_area()
        200
        """

        return self.ancho * self.alto


class ColeccionRectangulos:

    def __init__(self):
        """ (ColeccionRectangulos) -> NoneType

        >>> rc = ColeccionRectangulos()
        >>> rc.rectangulos
        []
        """