class Evento:    
    """Un nuevo evento de calendario."""

    def __init__(self, hora_inicio, hora_fin, nombre_evento):
        """ (Evento, int, int, str) -> NoneType

        Precondicion: 0 <= hora_inicio < hora_fin <= 23
        
        Inicializa un nuevo evento que comienza en hora_inicio, termina en hora_fin,
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

    def se_superpone(self, otro):
        """ (Evento, Evento) -> bool

        Devuelve True si y solo si este evento se superpone con el evento otro.

        >>> e1 = Evento(6, 7, 'Correr')
        >>> e2 = Evento(0, 7, 'Dormir')
        >>> e1.se_superpone(e2)
        True
        """

        return not (otro.hora_fin <= self.hora_inicio \\
                    or otro.hora_inicio >= self.hora_fin)

class Dia:
    """Un dia de calendario y sus eventos."""

    def __init__(self, dia=1, mes='Enero', ano=2014):
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

        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.eventos = []


    def programar_evento(self, nuevo_evento):
        """ (Dia, Evento) -> bool

        Programa nuevo_evento en este dia si y solo si no se superpone con
        eventos existentes. Devuelve True si y solo si nuevo_evento es programado.


        >>> d = Dia(3, 'Diciembre', 2014)
        >>> e = Evento(17, 23, 'Celebrar fin de clases')
        >>> d.programar_evento(e)
        True
        >>> d.eventos[0] == e
        True        
        """

        for evento_existente in self.eventos:
            if evento_existente.se_superpone(nuevo_evento):
                return False

        self.eventos.append(nuevo_evento)
        return True
    
    
    def programar_multiples_eventos(self, lista_eventos):
        """ (Dia, lista de Evento) -> int
        
        Devuelve el numero de eventos en lista_eventos que fueron programados 
        exitosamente en este dia, sin superponerse con eventos existentes.
        
        >>> d = Dia(5, 'Diciembre', 2015)
        >>> e1 = Evento(12, 16, 'Estudiar')
        >>> d.programar_evento(e1)
        True
        >>> e2 = Evento(17, 19, 'Cena con A')
        >>> e3 = Evento(11, 13, 'Almuerzo con B')
        >>> e4 = Evento(9, 10, 'Gimnasio')
        >>> d.programar_multiples_eventos([e2, e3, e4])
        2
        """