
class SistemaDeBienesRaices:
    def __init__(self):
        """ (SistemaDeBienesRaices)
        Inicializar la lista de casas
        """
        self.casas = []
        
    def anadir_casa(self, casa):
        """ (SistemaDeBienesRaices, Casa) -> NoneType
        Anadir una casa a nuestro sistema
        """
        self.casas.append(casa)
    
    def extraer_precio_minimo(self):
        """ (SistemaDeBienesRaices) -> int
        Devolver la casa con el precio mas bajo en el sistema, o -1 si no hay casas en el sistema
        """
        # completa este codigo


class Casa:
    """ Una instancia de una casa """
    def __init__(self, precio):
        """ (Casa, float)
        Inicializar una casa
        """
        self.precio = precio