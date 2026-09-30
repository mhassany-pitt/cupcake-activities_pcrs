class iPod:    
    def __init__(self, capacidad_max_canciones):
        self.capacidad_max_canciones = capacidad_max_canciones
        self.biblioteca = {}
        self.num_canciones = 0
    
    def espacio_disponible(self):
        #escribe este metodo
    
    def anadir_cancion(self, artista, nombre_cancion):
        if self.espacio_disponible() == 0:
            print("No hay mas espacio para canciones")
        else:

            #escribe el codigo faltante

            print(nombre_cancion + " de " + artista + " fue anadida a la biblioteca de musica")
            
    def cancion_en_biblioteca(self, artista, nombre_cancion):
        """ (iPod, str, str) -> bool
        devuelve verdadero si nombre_cancion de artista esta en la biblioteca"""

        #escribe el codigo faltante

    def eliminar_cancion(self, artista, nombre_cancion):
        """elimina artista si no hay canciones de artista"""
        if not self.cancion_en_biblioteca(artista, nombre_cancion):
            print("Cancion no encontrada")
        else:

            #escribe el codigo faltante

            print(nombre_cancion + " de " + artista + " fue eliminada de la biblioteca de musica")  