
class Item:
    #'una clase Item para el catalogo'
    internal_id = 100
    def __init__(self):
        Item.internal_id += 1
        self.id = Item.internal_id
        self.cantidad = 0
        # Otros atributos pueden ser definidos a continuacion. Este codigo esta oculto. Vea la descripcion para detalles.
        # ...
        
class Catalog:
    #'una clase Catalog simple'
    
    def __init__(self):
        #'el constructor'
        self.items=[]
        
    def agregar(self, item):
        #'agregar un item al catalogo'
        return self.items.append(item)
    
    def tiene_estilo(self, estilo_deseado):
        #'''devuelve verdadero si el catalogo tiene un item del estilo dado'''
        for obj in self.items:
            if obj.estilo == estilo_deseado:
                return True
        return False
    
    def tamano(self):
        #'''devuelve el numero de items en el catalogo'''
        return len(self.items)

    # Escriba el metodo busqueda aqui:
    def busqueda(self, forma_deseada):
        #'''devuelve el nombre del primer item que coincide con la forma dada'''
        