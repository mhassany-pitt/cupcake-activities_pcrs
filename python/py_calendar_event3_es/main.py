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
    
        # TODO: completar el cuerpo de este metodo.

    def renombrar(self, nuevo_nombre):
        """ (Evento, str) -> NoneType

        Cambia el nombre de este evento a nuevo_nombre.
        
        >>> e = Evento(12, 13, 'Almuerzo')
        >>> e.renombrar('Horas de oficina')
        >>> e.nombre
        'Horas de oficina'
        """
        
        # TODO: completar el cuerpo de este metodo.


    def duracion(self):
        """ (Evento) -> int

        Devuelve la duracion de este evento.

        >>> e = Evento(10, 11, 'Clase')
        >>> e.duracion()
        1
        """
        
        # TODO: completar el cuerpo de este metodo.

    
    def __str__(self):
        """ (Evento) -> str

        Devuelve una representacion en string de este evento.

        >>> e = Evento(6, 7, 'Correr')
        >>> str(e)
        'Correr: de 6 a 7'
        """
        
        # TODO: completar el cuerpo de este metodo.
              

    def __eq__(self, otro):
        """ (Evento, Evento) -> bool

        Devuelve True si y solo si este evento tiene la misma hora de inicio, hora de fin, 
        y nombre que otro.

        >>> e1 = Evento(6, 7, 'Correr')
        >>> e2 = Evento(6, 7, 'Correr')
        >>> e1 == e2
        True
        """
        
        # TODO: completar el cuerpo de este metodo.


    def se_superpone(self, otro):
        """ (Evento, Evento) -> bool

        Devuelve True si y solo si este evento se superpone con el evento otro.

        >>> e1 = Evento(6, 7, 'Correr')
        >>> e2 = Evento(0, 7, 'Dormir')
        >>> e1.se_superpone(e2)
        True
        """

        # TODO: completar el cuerpo de este metodo.