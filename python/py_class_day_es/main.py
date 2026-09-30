
class Evento:    
    """Un nuevo evento de calendario."""

    def __init__(self, hora_inicio, hora_fin, nombre_evento):
        """ (Evento, int, int, str) -> NoneType

        Precondicion: 0 <= hora_inicio < hora_fin <= 23
        
        Inicializa un nuevo evento que comienza a la hora_inicio, termina a la hora_fin,
        y se llama nombre.

        >>> e = Evento(12, 13, 'Almuerzo')
        >>> e.hora_inicio
        12
        >>> e.hora_fin
        13
        >>> e.nombre
        'Almuerzo'
        """
        
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.nombre = nombre_evento

    def __str__(self):
        """ (Evento) -> str

        Devuelve una representacion en string de este evento.

        >>> e = Evento(6, 7, 'Correr')
        >>> str(e)
        'Correr: de 6 a 7'
        """
        
        return '{0}: de {1} a {2}'.format(self.nombre, self.hora_inicio,
                                          self.hora_fin)

class Dia:
    """Un dia de calendario y sus eventos."""

    def __init__(self, dia, mes, ano):
        """ (Dia, int, str, int) -> NoneType

        Inicializa un dia en el calendario con dia, mes y ano,
        y sin eventos.

        >>> d = Dia(5, 'Abril', 2014)
        >>> d.dia
        5
        >>> d.mes
        'Abril'
        >>> d.ano
        2014
        >>> d.eventos
        []
        """

        # Por hacer: Completa el cuerpo de este metodo.

    def programar_evento(self, nuevo_evento):
        """ (Dia, Evento) -> NoneType
        
        Programa nuevo_evento en este dia, incluso si se superpone con
        un evento existente. Mas adelante mejoraremos este metodo.
        
        >>> d = Dia(26, 'Marzo', 2014)
        >>> e = Evento(11, 12, 'Reunion')
        >>> d.programar_evento(e)
        >>> d.eventos[0] == e
        True
        """

        # Por hacer: Completa el cuerpo de este metodo.
    
    def __str__(self):
        """ (Dia) -> str
    
        Devuelve una representacion en string de este dia.
        
        >>> d = Dia(4, 'Abril', 2014)
        >>> d.programar_evento(Evento(13, 14, 'Entregar ultimo ejercicio'))
        >>> d.programar_evento(Evento(19, 23, 'Celebrar fin de clases'))
        >>> print(d)
        4 Abril 2014:
        - Entregar ultimo ejercicio: de 13 a 14
        - Celebrar fin de clases: de 19 a 23
        """

        # Por hacer: Completa el cuerpo de este metodo.