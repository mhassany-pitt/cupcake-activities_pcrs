class Usuario:
    
    def __init__(self, nombre_usuario, contrasena, info_cuenta):
        """ (Usuario, str, str, str) -> NoneType
        
        Inicializa el usuario con nombre_usuario, contrasena e info_cuenta.
        
        >>> nuevo_usuario = Usuario('xyz', 'contrasena1', "Banco en Linea de Bob")
        >>> nuevo_usuario.nombre_usuario
        'xyz'
        >>> nuevo_usuario.contrasena
        'contrasena1'
        >>> nuevo_usuario.info_cuenta
        "Banco en Linea de Bob"
        """
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.info_cuenta = info_cuenta
        
    def iniciar_sesion(self, contrasena_ingresada):
        """ (Usuario, str) -> bool
        
        Devuelve True si y solo si la contrasena del usuario coincide con contrasena_ingresada.
        
        >>> nuevo_usuario = Usuario('xyz', 'contrasena1', "Banco en Linea de Bob")
        >>> nuevo_usuario.iniciar_sesion('contrasena1')
        True
        >>> nuevo_usuario.iniciar_sesion('1234')
        False
        """
        return self.contrasena == contrasena_ingresada

    def actualizar_cuenta(self, contrasena_ingresada, nueva_info):
        """ (Usuario, str, str) -> NoneType
        
        Modifica la info_cuenta del usuario para ser nueva_info si la contrasena del usuario
        coincide con contrasena_ingresada.
        
        >>> nuevo_usuario = Usuario('xyz', 'contrasena1', "Banco en Linea de Bob")
        >>> nuevo_usuario.actualizar_cuenta('1234', 'B.O.B.')
        >>> nuevo_usuario.info_cuenta
        "Banco en Linea de Bob"
        >>> nuevo_usuario.actualizar_cuenta('contrasena1', 'B.O.B.')
        >>> nuevo_usuario.info_cuenta
        'B.O.B.'
        """