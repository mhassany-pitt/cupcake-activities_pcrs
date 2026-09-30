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


    def renombrar(self, nuevo_nombre):
        """ (Evento, str) -> NoneType

        Cambia el nombre de este evento a nuevo_nombre.
        
        #TODO: completa el ejemplo a continuacion usando el metodo renombrar.
        >>> e = Evento(12, 13, 'Almuerzo')
        >>>
        >>>

        """